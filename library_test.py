from dotenv import load_dotenv
load_dotenv()

from spec2chat import run_chatbot

user_input = "I want a cheap vegetarian restaurant"
user_answers = []
filledslots = {}

print("\n[Paso 0] Enviando primer mensaje:")
response = run_chatbot(user_input=user_input)
print("[Paso 1] Respuesta del chatbot:")
print(response)

# Guardar datos comunes
tasks = response.get("tasks", {})
domain = response.get("dom", "")
intent = response.get("intent", "")
reqslots = response.get("reqslots", [])
services = response.get("services", [])

# Bucle mientras no se llegue al final de la conversación
paso = 2
while not response.get("end_of_conversation", False):
    print(f"\n[Paso {paso}] Enviando respuestas a nuevas preguntas...")

    # Generar respuestas simuladas
    simulated_answers = {
        "name": "John Doe",
        "phone": "123456789",
        "date": "2024-06-01",
        "time": "19:30",
        "diners": "2",
        "location": "terrace",
        "food": "vegetarian",
        "pricerange": "cheap",
        "terrace": "yes",
        "petfriendly": "no",
        "smokingzone": "no",
        "smoking": "no"
    }

    # Responder a preguntas
    for slot, question in response["questions"].items():
        answer = simulated_answers.get(slot, "test")
        user_answers.append({"chatbot": question, "user": answer})
        filledslots[slot] = answer

    # Nueva llamada al chatbot
    response = run_chatbot(
        user_input=user_input,
        user_answers=user_answers,
        tasks=response.get("tasks", tasks),
        domain=response.get("dom", domain),
        intent=response.get("intent", intent),
        filledslots=filledslots,
        services=response.get("services", services),
        reqslots=response.get("reqslots", reqslots),
        service_id=response.get("service_id")
    )

    print(f"[Paso {paso}] Respuesta:")
    print(response)

    # ✅ Salir si ya no quedan preguntas y la conversación se marca como final
    if response.get("final") and not response.get("questions"):
        print("[DEBUG] Finalizado: todos los slots completados.")
        break

    paso += 1

# Fin del flujo
if response.get("end_of_conversation"):
    print("\n✅ Conversación finalizada correctamente.")
else:
    print("\n❓ Aún faltan datos o no se pudo continuar.")