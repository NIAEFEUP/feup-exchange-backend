from drf_yasg import openapi

TestServiceSuccessResponse = \
    openapi.Response(
        description="OK",
        schema=openapi.Schema(
            title="Test Service",
            type=openapi.TYPE_OBJECT,
            properties={
                "message": openapi.Response(
                    type=openapi.TYPE_STRING,
                    enum=["Yep, it\'s working!"],
                    description="Message indicating that the service is "
                                "available and functioning properly."
                ),
            },
        )
    )
