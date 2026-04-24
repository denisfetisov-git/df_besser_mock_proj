import React from "react";
import { TableBlock } from "../components/runtime/TableBlock";

const Home: React.FC = () => {
  return (
    <div id="9VNa8scBXvnTxdC4">
    <TableBlock id="ibvt" styles={{"width": "100%", "minHeight": "400px", "--chart-color-palette": "default"}} title="DOCS" options={{"showHeader": true, "stripedRows": false, "showPagination": true, "rowsPerPage": 5, "actionButtons": true, "columns": [{"label": "Name", "column_type": "field", "field": "name", "type": "str", "required": true}, {"label": "Date", "column_type": "field", "field": "date", "type": "date", "required": true}, {"label": "ID", "column_type": "field", "field": "ID", "type": "int", "required": true}], "formColumns": [{"column_type": "field", "field": "name", "label": "name", "type": "str", "required": true, "defaultValue": null}, {"column_type": "field", "field": "date", "label": "date", "type": "date", "required": true, "defaultValue": null}, {"column_type": "field", "field": "ID", "label": "ID", "type": "int", "required": true, "defaultValue": null}]}} dataBinding={{"entity": "Documents", "endpoint": "/documents/"}} />    </div>
  );
};

export default Home;
