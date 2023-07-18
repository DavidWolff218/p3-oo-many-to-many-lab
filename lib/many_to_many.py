class Author:
    
    all = []
    
    def __init__(self, name):
        self.name = name
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    # why the return needed here
    
    def total_royalties(self):
        royalties = [contract.royalties for contract in self.contracts()]
        return sum(royalties)


class Book:
    
    all = []
    
    def __init__(self, title):
        self.title = title
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    
    all = []
    
    def __init__(self, author, book, date, royalties):
        
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author class")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book class")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        
        Contract.all.append(self)
        
    @classmethod    
    def contracts_by_date(cls):
        return sorted(Contract.all, key=lambda contract: contract.date)
       

        