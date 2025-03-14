import chromadb

print("Ingesting data into ChromaDB")
chroma_client = chromadb.Client()

# Create a collection
collection_name = "my_doc"
collection = chroma_client.create_collection(name="my_doc")

# Folder containing the documents
folder = "app/documents"

# Ingest the documents
collection.ingest_documents_from_folder(folder)
print("Ingestion complete")

# Query the collection
query = "select * from my_doc"
results = collection.query(query)
print(results)
