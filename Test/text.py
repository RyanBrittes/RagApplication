from nomic import embed
            
output = embed.text(
    texts=['document 1'],
    model='nomic-embed-text-v1.5',
    task_type='search_document', 
)

print(output)