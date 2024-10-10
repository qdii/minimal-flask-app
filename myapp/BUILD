load("@aspect_rules_py//py:defs.bzl", "py_library")
load("@rules_apko//apko:defs.bzl", "apko_image")
load("@rules_oci//oci:defs.bzl", "oci_push")
load("@pip//:requirements.bzl", "requirement")
load("//:py_layer.bzl", "py_oci_image")

py_binary(
  name = "myapp",
  srcs = [":myapp.py"],
  deps = [
    requirement("flask"),
    requirement("gunicorn"),
  ],
  args = ["myapp.myapp:app"],
)

# Alpine base image
apko_image(
  name = "base",
  architecture = "amd64",
  config = "apko.yaml",
  contents = "@apko_lock//:contents",
  tag = "myapp:latest",
)

py_oci_image(
  name = "image",
  base = ":base",
  binary = ":myapp",
  entrypoint = ["/myapp/myapp"],
)

oci_push(
  name = "push",
  image = ":image",
  remote_tags = ["0.0.1"],
  repository = "index.docker.io/qdii/myapp",
)

