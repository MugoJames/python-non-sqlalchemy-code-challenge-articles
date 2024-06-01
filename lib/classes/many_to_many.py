class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        if not isinstance (title,str):
            raise TypeError("Author must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters long")
        Article.all.append(self)

class Author:
    def __init__(self, name):
        if not isinstance (name,str):
            raise TypeError("Author name must be a string")
        if len (name) == 0:
            raise ValueError("Author name cannot be empty")

        self._name = name
    @property
    def name(self):
        return self._name
####################################################################################3

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self,magazine,title)

    def topic_areas(self):
        return(
            list({magazine.category for magazine in self.magazines()})
            if self.magazines()
            else None
        )

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if not isinstance(value,str):
             raise TypeError("Magazine name must be a string")
        if not 2 <= len(value) <= 16:
            raise ValueError("Magazine name must be between 2 and 16 characters")
        self._name = value
#############################################################################################
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if not isinstance (category,str):
            raise TypeError("Category must be a string")
        if len(category) == 0:
            raise ValueError("Category cannot be empty")
        self._category = category
 #################################################################################################3



    def articles(self):
        return [article for article in Article.all if article.magazine == self ]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        articles = self.articles()
        return [article.title for article in articles] if articles else None



    def contributing_authors(self):
        non_unique_authors = [article.author for article in self.articles()]
        if unique_contributors := list(
            {
                author
                for author in non_unique_authors
                if non_unique_authors.count(author) > 2
            }
        ):
            return unique_contributors
