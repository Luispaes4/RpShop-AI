from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  # Permite que sua loja virtual se comunique com o servidor da IA

# Configuração da API Key fornecida
openai.api_key = "Q.Ab8RN6K5SGm3MbtFjog0V84NXxPdDw3Qwu1C7Zm0kMn7V8YLbA"

# Contexto de comportamento da IA (Altere os detalhes para combinar com a sua loja)
CONTEXTO_LOJA = (
    "Você é o 'E-Bot', o assistente virtual de uma loja virtual premium. "
    "Seu objetivo é ser extremamente educado, profissional, prestativo e focado em vendas. "
    "Ajude os clientes a encontrar produtos, tire dúvidas sobre frete (diga que calculamos no carrinho) "
    "e política de devolução (até 7 dias). Seja conciso e use emojis de forma moderada e elegante."
)

@app.route("/chat", methods=["POST"])
def chat():
    dados = request.get_json()
    mensagem_usuario = dados.get("mensagem", "")

    if not mensagem_usuario:
        return jsonify({"erro": "Mensagem vazia"}), 400

    try:
        # Chamada oficial para a API de Chat
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", # Ou gpt-4o se sua chave permitir
            messages=[
                {"role": "system", "content": CONTEXTO_LOJA},
                {"role": "user", "content": mensagem_usuario}
            ],
            temperature=0.7
        )
        
        resposta_ia = resposta.choices[0].message['content']
        return jsonify({"resposta": resposta_ia})

    except Exception as e:
        return jsonify({"erro": f"Erro ao processar: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
