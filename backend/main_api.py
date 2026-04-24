import uvicorn
import os, json
import time as time_module
import logging
from fastapi import Depends, FastAPI, HTTPException, Request, status, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from pydantic_classes import *
from sql_alchemy import *

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

############################################
#
#   Initialize the database
#
############################################

def init_db():
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data/Class_Diagram.db")
    # Ensure local SQLite directory exists (safe no-op for other DBs)
    os.makedirs("data", exist_ok=True)
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
        pool_size=10,
        max_overflow=20,
        pool_pre_ping=True,
        echo=False
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    return SessionLocal

app = FastAPI(
    title="Class_Diagram API",
    description="Auto-generated REST API with full CRUD operations, relationship management, and advanced features",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_tags=[
        {"name": "System", "description": "System health and statistics"},
        {"name": "Documents", "description": "Operations for Documents entities"},
    ]
)

# Enable CORS for all origins (for development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

############################################
#
#   Middleware
#
############################################

# Request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log all incoming requests and responses."""
    logger.info(f"Incoming request: {request.method} {request.url.path}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response

# Request timing middleware
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """Add processing time header to all responses."""
    start_time = time_module.time()
    response = await call_next(request)
    process_time = time_module.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

############################################
#
#   Exception Handlers
#
############################################

# Global exception handlers
@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    """Handle ValueError exceptions."""
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": "Bad Request",
            "message": str(exc),
            "detail": "Invalid input data provided"
        }
    )


@app.exception_handler(IntegrityError)
async def integrity_error_handler(request: Request, exc: IntegrityError):
    """Handle database integrity errors."""
    logger.error(f"Database integrity error: {exc}")

    # Extract more detailed error information
    error_detail = str(exc.orig) if hasattr(exc, 'orig') else str(exc)

    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "error": "Conflict",
            "message": "Data conflict occurred",
            "detail": error_detail
        }
    )


@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_error_handler(request: Request, exc: SQLAlchemyError):
    """Handle general SQLAlchemy errors."""
    logger.error(f"Database error: {exc}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "Internal Server Error",
            "message": "Database operation failed",
            "detail": "An internal database error occurred"
        }
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Handle HTTP exceptions with consistent format."""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail if isinstance(exc.detail, str) else "HTTP Error",
            "message": exc.detail,
            "detail": f"HTTP {exc.status_code} error occurred"
        }
    )

# Initialize database session
SessionLocal = init_db()
# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        logger.error("Database session rollback due to exception")
        raise
    finally:
        db.close()

############################################
#
#   Global API endpoints
#
############################################

@app.get("/", tags=["System"])
def root():
    """Root endpoint - API information"""
    return {
        "name": "Class_Diagram API",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health", tags=["System"])
def health_check():
    """Health check endpoint for monitoring"""
    from datetime import datetime
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "database": "connected"
    }


@app.get("/statistics", tags=["System"])
def get_statistics(database: Session = Depends(get_db)):
    """Get database statistics for all entities"""
    stats = {}
    stats["documents_count"] = database.query(Documents).count()
    stats["total_entities"] = sum(stats.values())
    return stats


############################################
#
#   BESSER Action Language standard lib
#
############################################


async def BAL_size(sequence:list) -> int:
    return len(sequence)

async def BAL_is_empty(sequence:list) -> bool:
    return len(sequence) == 0

async def BAL_add(sequence:list, elem) -> None:
    sequence.append(elem)

async def BAL_remove(sequence:list, elem) -> None:
    sequence.remove(elem)

async def BAL_contains(sequence:list, elem) -> bool:
    return elem in sequence

async def BAL_filter(sequence:list, predicate) -> list:
    return [elem for elem in sequence if predicate(elem)]

async def BAL_forall(sequence:list, predicate) -> bool:
    for elem in sequence:
        if not predicate(elem):
            return False
    return True

async def BAL_exists(sequence:list, predicate) -> bool:
    for elem in sequence:
        if predicate(elem):
            return True
    return False

async def BAL_one(sequence:list, predicate) -> bool:
    found = False
    for elem in sequence:
        if predicate(elem):
            if found:
                return False
            found = True
    return found

async def BAL_is_unique(sequence:list, mapping) -> bool:
    mapped = [mapping(elem) for elem in sequence]
    return len(set(mapped)) == len(mapped)

async def BAL_map(sequence:list, mapping) -> list:
    return [mapping(elem) for elem in sequence]

async def BAL_reduce(sequence:list, reduce_fn, aggregator) -> any:
    for elem in sequence:
        aggregator = reduce_fn(aggregator, elem)
    return aggregator


############################################
#
#   Documents functions
#
############################################

@app.get("/documents/", response_model=None, tags=["Documents"])
def get_all_documents(detailed: bool = False, database: Session = Depends(get_db)) -> list:
    from sqlalchemy.orm import joinedload

    return database.query(Documents).all()


@app.get("/documents/count/", response_model=None, tags=["Documents"])
def get_count_documents(database: Session = Depends(get_db)) -> dict:
    """Get the total count of Documents entities"""
    count = database.query(Documents).count()
    return {"count": count}


@app.get("/documents/paginated/", response_model=None, tags=["Documents"])
def get_paginated_documents(skip: int = 0, limit: int = 100, detailed: bool = False, database: Session = Depends(get_db)) -> dict:
    """Get paginated list of Documents entities"""
    total = database.query(Documents).count()
    documents_list = database.query(Documents).offset(skip).limit(limit).all()
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": documents_list
    }


@app.get("/documents/search/", response_model=None, tags=["Documents"])
def search_documents(
    database: Session = Depends(get_db)
) -> list:
    """Search Documents entities by attributes"""
    query = database.query(Documents)


    results = query.all()
    return results


@app.get("/documents/{documents_id}/", response_model=None, tags=["Documents"])
async def get_documents(documents_id: int, database: Session = Depends(get_db)) -> Documents:
    db_documents = database.query(Documents).filter(Documents.id == documents_id).first()
    if db_documents is None:
        raise HTTPException(status_code=404, detail="Documents not found")

    response_data = {
        "documents": db_documents,
}
    return response_data



@app.post("/documents/", response_model=None, tags=["Documents"])
async def create_documents(documents_data: DocumentsCreate, database: Session = Depends(get_db)) -> Documents:


    db_documents = Documents(
        name=documents_data.name,        date=documents_data.date,        ID=documents_data.ID        )

    database.add(db_documents)
    database.commit()
    database.refresh(db_documents)




    return db_documents


@app.post("/documents/bulk/", response_model=None, tags=["Documents"])
async def bulk_create_documents(items: list[DocumentsCreate], database: Session = Depends(get_db)) -> dict:
    """Create multiple Documents entities at once"""
    created_items = []
    errors = []

    for idx, item_data in enumerate(items):
        try:
            # Basic validation for each item

            db_documents = Documents(
                name=item_data.name,                date=item_data.date,                ID=item_data.ID            )
            database.add(db_documents)
            database.flush()  # Get ID without committing
            created_items.append(db_documents.id)
        except Exception as e:
            errors.append({"index": idx, "error": str(e)})

    if errors:
        database.rollback()
        raise HTTPException(status_code=400, detail={"message": "Bulk creation failed", "errors": errors})

    database.commit()
    return {
        "created_count": len(created_items),
        "created_ids": created_items,
        "message": f"Successfully created {len(created_items)} Documents entities"
    }


@app.delete("/documents/bulk/", response_model=None, tags=["Documents"])
async def bulk_delete_documents(ids: list[int], database: Session = Depends(get_db)) -> dict:
    """Delete multiple Documents entities at once"""
    deleted_count = 0
    not_found = []

    for item_id in ids:
        db_documents = database.query(Documents).filter(Documents.id == item_id).first()
        if db_documents:
            database.delete(db_documents)
            deleted_count += 1
        else:
            not_found.append(item_id)

    database.commit()

    return {
        "deleted_count": deleted_count,
        "not_found": not_found,
        "message": f"Successfully deleted {deleted_count} Documents entities"
    }

@app.put("/documents/{documents_id}/", response_model=None, tags=["Documents"])
async def update_documents(documents_id: int, documents_data: DocumentsCreate, database: Session = Depends(get_db)) -> Documents:
    db_documents = database.query(Documents).filter(Documents.id == documents_id).first()
    if db_documents is None:
        raise HTTPException(status_code=404, detail="Documents not found")

    setattr(db_documents, 'name', documents_data.name)
    setattr(db_documents, 'date', documents_data.date)
    setattr(db_documents, 'ID', documents_data.ID)
    database.commit()
    database.refresh(db_documents)

    return db_documents


@app.delete("/documents/{documents_id}/", response_model=None, tags=["Documents"])
async def delete_documents(documents_id: int, database: Session = Depends(get_db)):
    db_documents = database.query(Documents).filter(Documents.id == documents_id).first()
    if db_documents is None:
        raise HTTPException(status_code=404, detail="Documents not found")
    database.delete(db_documents)
    database.commit()
    return db_documents








############################################
# Maintaining the server
############################################
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



