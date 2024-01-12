import reflex as rx

def header() -> rx.Component :
    return rx.vstack(
        rx.avatar(name="Brandon Bustos", size="xl"),
        rx.text("@lineasdecodigo"),
        rx.text("Hola 👋 Mi nombre es Brandon Bustos"),
        rx.text("""
                Soy tecnologo en sistemas y desarrolladore de software desde hace 3 años, Trabajo con lenguajes de 
                programacion como C#, Python y Java.
                Bienvenid@!!
                """)
    )