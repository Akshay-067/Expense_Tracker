class expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    title = Column(String)
    amount = Column(Integer)
    category = Column(String)
    expense_date = Column(Datetime)
    created_at = Column(Dtaetime , default=datetime.now)