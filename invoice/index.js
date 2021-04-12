const express = require("express");
const ejs = require("ejs");
const bodyParser = require("body-parser");
const path = require('path');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.set("view engine", "ejs");

app.get("/", function (req, res) {
  res.render("index");
});
var invoice_number=1;
app.post("/", function (req, res) {
  const { createInvoice } = require("./createInvoice.js");
  const invoice = {
    shipping: req.body.shipping,
    items: [req.body.item
    ],
    subtotal: req.body.item.amount*req.body.item.quantity,
    paid: 0,
    invoice_nr: invoice_number,
  };
  createInvoice(invoice, "invoice.pdf");
  console.log(req.body.shipping);
  res.redirect('/');
  invoice_number=invoice_number+1;
});

app.listen(3000, function () {
  console.log("Server has Started at port 3000");
});
