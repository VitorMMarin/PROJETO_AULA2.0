from ..extensions import db

class Cadastro(db.Model):
    __tablename__= "Cadastros"
    id= db.column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    RG = db.Column(db.String(10))
    CPF = db.Column(db.String(12))
    rua = db.Column(db.String(150))
    numero = db.Column(db.Stringr(10))
    bairro = db.Column(db.String(150))
    cidade = db.Column(db.String(150))
    estado = db.Column(db.String(150))
    inicio = db.Column(db.Date)
    fim = db.Column(db.Date)

    def __repr__(self):
        return "<Cadastro(nome={}, RG={},CPF={},rua={},numero={},bairro={},cidade={},estado={} inicio={},fim={})>".format(self.nome, self.RG,self.CPF,self.rua,self.numero,self.bairro,self.cidade,self.estado, self.inicio, self.fim)
