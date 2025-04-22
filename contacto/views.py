from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import FormularioContacto
from django.conf import settings  # 👈 Importas aquí

def contacto(request):
    formulario_contacto = FormularioContacto()
    enviado = False

    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            correo = request.POST.get("email")
            contenido = request.POST.get("contenido")

            # 👇 Verificación en consola
            print("💡 EMAIL HOST:", settings.EMAIL_HOST)

            email = EmailMessage(
                "Mensaje desde App Django",
                "El usuario {} con la dirección {} escribe lo siguiente:\n\n{}".format(nombre, correo, contenido),
                settings.EMAIL_HOST_USER,
                ["agenciajm123@gmail.com"],  # Puedes cambiar por otro si lo necesitas
                reply_to=[correo]
            )

            try:
                email.send()
                print("Correo enviado correctamente")
                return redirect("/contacto/?valido=True")
            except Exception as e:
                print("ERROR AL ENVIAR CORREO:", e)
                return redirect("/contacto/?novalido=True")

    enviado = 'valido' in request.GET
    return render(request, "contacto/contacto.html", {
        'miFormulario': formulario_contacto,
        'enviado': enviado
    })
