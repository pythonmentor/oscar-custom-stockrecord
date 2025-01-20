from oscar.apps.dashboard.catalogue.forms import StockRecordForm as CoreStockRecordForm


class StockRecordForm(CoreStockRecordForm):
    class Meta(CoreStockRecordForm.Meta):
        fields = [
            "partner",
            "partner_sku",
            "price_currency",
            "price",
            "num_in_stock",
            "low_stock_threshold",
            "cost_price",
        ]
