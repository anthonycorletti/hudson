import time

from docarray import Document, DocumentArray

from hudson import hudson_client

#
#   Create a namespace.
#
print("๐ Creating a namespace")
namespace = hudson_client.create_namespace(
    name="video-example",
)

#
#   Create a dataset.
#
print("๐ Creating a dataset")
dataset = hudson_client.create_dataset(
    namespace_id=namespace.id,
    name="video-example-dataset",
)

#
#   Write a DocumentArray to the dataset.
#
print("๐งฑ Building the dataset")
n = 100
data = DocumentArray(
    [Document(uri="https://docarray.jina.ai/_static/mov_bbb.mp4") for _ in range(n)]
)

print("โ๏ธ  Writing to the dataset")
t0 = time.time()
hudson_client.write_dataset(
    namespace_id=namespace.id,
    dataset_id=dataset.id,
    data=data,
)
print(f"โฐ Took {time.time() - t0:.2f} seconds to write {n} documents")


print("๐ Reading from the dataset")
t0 = time.time()
da = hudson_client.read_dataset(
    namespace_id=namespace.id,
    dataset_id=dataset.id,
)
print(f"โฐ Took {time.time() - t0:.2f} seconds to read {n} documents")

print("๐งน Cleaning up!")
hudson_client.delete_namespace(namespace.id)
