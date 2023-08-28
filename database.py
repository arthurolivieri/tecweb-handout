import sqlite3

class Database:
    def __init__(self, nomeDB) -> None:
        self.nomeDB = nomeDB
        self.conn = sqlite3.connect(nomeDB + '.db')
        self.conn.execute('CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL UNIQUE);')

    def add(self, note):
        self.query = "INSERT OR REPLACE INTO note (title,content) VALUES (?,?);"
        self.conn.execute(self.query, (note.title, note.content))
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        lista = []
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            lista.append(Note(id, title, content))
        return lista

    def update(self, entry):
        query = 'UPDATE note SET title = ?, content = ? WHERE id = ?;'
        self.conn.execute(query, (entry.title, entry.content, entry.id))
        self.conn.commit()

    def delete(self, note_id):
        query = 'DELETE FROM note WHERE id = ?;'
        self.conn.execute(query, (note_id,))
        self.conn.commit()


from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''