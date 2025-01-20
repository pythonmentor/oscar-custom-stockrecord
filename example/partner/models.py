from decimal import Decimal
from django.db import models
from django.utils.translation import gettext_lazy as _
from oscar.apps.partner.abstract_models import AbstractStockRecord


class StockRecord(AbstractStockRecord):
    # Ajouter un champ pour le coût de revient
    cost_price = models.DecimalField(
        _("Cost Price"), decimal_places=2, max_digits=12, blank=True, null=True
    )

    def calculate_margin(self):
        """
        Calculer la marge brute (prix - coût de revient).
        Retourne la marge en tant que valeur décimale ou None si l'un des champs est manquant.
        """
        if self.price is None or self.cost_price is None:
            return None
        return self.price - self.cost_price

    def get_margin_percentage(self):
        """
        Retourne la marge brute en pourcentage (par rapport au prix de vente).
        """
        if self.price is None or self.cost_price is None or self.price == 0:
            return None
        margin = self.calculate_margin()
        return (margin / self.price) * Decimal(100)


from oscar.apps.partner.models import *  # noqa
