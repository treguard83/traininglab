app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@127.0.0.1/testdb"
app.config['SECRET_KEY'] = "TEST"
db = SQLAlchemy(app)
db.create_all()
from application import routes