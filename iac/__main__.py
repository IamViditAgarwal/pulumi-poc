"""A Google Cloud Python Pulumi program"""

import pulumi
# from pulumi_gcp import storage

import pulumi_gcp as gcp

# Creating the function to create the bucket
def pg_bucket(bkt_name):
  bucket = gcp.storage.Bucket(bkt_name,
    cors=[gcp.storage.BucketCorArgs(
        max_age_seconds=3600,
        methods=[
            "GET",
            "HEAD",
            "PUT",
            "POST",
            "DELETE",
        ],
        origins=["http://image-store.com"],
        response_headers=["*"],
    )],
    force_destroy=True,
    location="EU",
    name=bkt_name,
    uniform_bucket_level_access=True,
    website=gcp.storage.BucketWebsiteArgs(
        main_page_suffix="index.html",
        not_found_page="404.html",
    ))
  return bucket

# this function can be imported in other file
# bucket_obj = pg_bucket()

# Creating the function invoker
def pg_bucket_invoker(bucket_args):
  for _ in bucket_args:
    created_bkt = pg_bucket(_.get('name'))
    # Export the DNS name of the bucket
    pulumi.export(f"{_['name']}-id", created_bkt.id)
    # pulumi.export(, created_bkt.id)


global_bucket_args = [
  {
    'name': 'static-site11'
  },
  {
    'name': 'static-site123'
  },
  {
    'name': 'static-site12'
  }
]

# calling the invoker function
pg_bucket_invoker(global_bucket_args)