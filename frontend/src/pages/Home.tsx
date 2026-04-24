import React from "react";
import { TableBlock } from "../components/runtime/TableBlock";

const Home: React.FC = () => {
  return (
    <div id="ESDrluMjPMObIm2n">
    <div id="iu4f" className="gjs-row" style={{"width": "100%", "paddingTop": "10px", "paddingRight": "10px", "paddingBottom": "10px", "paddingLeft": "10px", "display": "flex", "--chart-color-palette": "default", "flexWrap": "wrap"}}>
      <div id="in99" className="gjs-cell" style={{"--chart-color-palette": "default", "flex": "1 1 calc(33.333% - 20px)", "minWidth": "250px"}} />
    </div>
    <p id="text">{"0"}</p>
    <TableBlock id="i0iu" styles={{"width": "100%", "minHeight": "400px", "--chart-color-palette": "default"}} title="Table Title" options={{"showHeader": true, "stripedRows": false, "showPagination": true, "rowsPerPage": 5, "actionButtons": true, "columns": [{"label": "Date", "column_type": "field", "field": "date", "type": "date", "required": true}, {"label": "ID", "column_type": "field", "field": "ID", "type": "int", "required": true}], "formColumns": [{"column_type": "field", "field": "name", "label": "name", "type": "str", "required": true, "defaultValue": null}, {"column_type": "field", "field": "date", "label": "date", "type": "date", "required": true, "defaultValue": null}, {"column_type": "field", "field": "ID", "label": "ID", "type": "int", "required": true, "defaultValue": null}]}} dataBinding={{"entity": "Documents", "endpoint": "/documents/"}} />    </div>
  );
};

export default Home;
