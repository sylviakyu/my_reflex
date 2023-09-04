import reflex as rx

class MyreflexConfig(rx.Config):
    pass

config = MyreflexConfig(
    app_name="my_reflex",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)