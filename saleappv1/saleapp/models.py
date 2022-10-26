from sqlalchemy import Column, Integer, String
from saleapp import db, app


class BaseModel(db.Model):
    # Lớp trừu tượng
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

if __name__ == '__main__':
    with app.app_context():
        c1 = Category(name='Điện thoại')
        c2 = Category(name='Máy tính bảng')
        c3 = Category(name='Phụ kiện')
        c4 = Category(name='Máy tính bàn')

        db.session.add_all([c1, c2, c3, c4])
        db.session.commit()
        # db.create_all()