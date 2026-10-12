from flask import Flask, jsonify
app = Flask(__name__)
prods = {1:'Notebook',2:'Celular',3:'fone'}
# professora, para acessar as informações da api tem que adicionar /prod/e o numero do item, não entendi direito como fazeer ir direto
@app.route('/prod/<int:id>')
def buscar(id):
    try:
        prod = prods[id]
        return jsonify({'produto':prod}),200
    except KeyError:
        return jsonify({'erro': 'produto não encotrado'}),404
    except Exception:
        return jsonify({'erro': 'erro do servidor'}),500
if __name__ == "__main__":
    app.run(debug=False)