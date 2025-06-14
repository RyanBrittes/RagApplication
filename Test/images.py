from nomic import embed
import numpy as np

output = embed.image(
    images=[
        "/home/ryan/Documents/AI/RagApp/Test/images/image01.png",
        "/home/ryan/Documents/AI/RagApp/Test/images/image02.png",
    ],
    model='nomic-embed-vision-v1.5',
)

print(output['usage'])
embeddings = np.array(output['embeddings'])
print(embeddings.shape)
