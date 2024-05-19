class Author:
    author_contracts = []
    contract = []



    def __init__(self, name: str) -> None:
        self.name = name 

    def contracts(self):
        list_of_contracts = [contract for contract in Contract.all if contract.author == self]
        return list_of_contracts
    
    def books(self):
        list_of_books = [contract.book for contract in Contract.all if contract.author == self]
        return list_of_books
    
    def sign_contract(self, book, date, royalties): 
        new_contract = Contract(self, book, date, royalties)
        self.author_contracts.append(new_contract)
        return new_contract
    
    def total_royalties(self):
        royalties_list = [contract.royalties for contract in self.contracts()]
        royalties_sum = sum(royalties_list)
        return(royalties_sum)
        

class Book:
    all = []
    def __init__(self, title: str): 
        self.title = title

    def contracts(self):
        list_of_books = [contract for contract in Contract.all if contract.book == self]
        return list_of_books

    def authors(self):
        list_of_authors = [contract.author for contract in Contract.all if contract.book == self]
        return list_of_authors
    

class Contract(Author, Book):
    all = []
    def __init__(self, author, book, date, royalties):
        assert isinstance(author, Author), "Invalid author"
        self.author = author

        assert isinstance(book, Book), "Invalid book"
        self.book = book

        assert isinstance(date, str), "Invalid date, type must be string"
        self.date = date

        assert isinstance(royalties, int), "Invalid royalties, type must be int"
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        list_by_date = [contract for contract in cls.all if contract.date == date]
        return(list_by_date)