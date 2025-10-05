import graphene

# ------------------------------
# Queries
# ------------------------------

class Query(graphene.ObjectType):
    # Example query just to test GraphQL
    hello = graphene.String(description="Simple hello world query")

    def resolve_hello(root, info):
        return "Hello from Core!"

# ------------------------------
# Mutations
# ------------------------------

class BaseMutation(graphene.Mutation):
    # All mutations in core can inherit from this if needed
    success = graphene.Boolean()
    message = graphene.String()

class TestMutation(BaseMutation):
    class Arguments:
        name = graphene.String(required=True)

    # Optional: return a value
    def mutate(self, info, name):
        return TestMutation(success=True, message=f"Hello, {name}!")

class Mutation(graphene.ObjectType):
    test_mutation = TestMutation.Field()
