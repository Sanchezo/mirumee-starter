import graphene

from .types import CheckoutType, CheckoutLineType, OrderType
from ...checkout.models import Checkout, CheckoutLine, Order
from .mutations import CheckoutCreate, CheckoutLineCreate
from ..core.utils import staff_member_required


class CheckoutQueries(graphene.ObjectType):
    checkout = graphene.Field(
        CheckoutType, id=graphene.Argument(graphene.ID)
    )

    checkout_line = graphene.Field(
        CheckoutLineType, id=graphene.Argument(graphene.ID)
    )
    order = graphene.Field(
        OrderType, id=graphene.Argument(graphene.ID)
    )
    checkouts = graphene.List(CheckoutType)

    def resolve_checkout(self, _info, id):
        checkout = Checkout.objects.filter(id=id).first()
        return checkout

    def resolve_checkout_line(self, _info, id):
        checkout_line = CheckoutLine.objects.filter(id=id).first()
        return checkout_line

    def resolve_order(self, _info, id):
        order = Order.objects.filter(id=id).first()

    @staff_member_required
    def resolve_checkouts(self, _info):
        checkouts = Checkout.objects.all()
        return checkouts


class CheckoutMutations(graphene.ObjectType):
    checkout_create = CheckoutCreate.Field()
    checkout_line_create = CheckoutLineCreate.Field()