import argparse
import io
import re
from google.cloud import vision

# [START vision_text_detection]
def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    # [START vision_python_migration_text_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))


# [START vision_text_detection_gcs]
def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))


def run_local(args):
    if args.command == 'text':
        detect_text(args.path)
    else:
        print('Error, path parameter is not null!')


def run_uri(args):
    if args.command == 'text-uri':
        detect_text_uri(args.uri)
    else:
        print('Error, url parameter is not null!')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest='command')

    detect_text_parser = subparsers.add_parser(
        'text', help=detect_text.__doc__)
    detect_text_parser.add_argument('path')

    text_file_parser = subparsers.add_parser(
        'text-uri', help=detect_text_uri.__doc__)
    text_file_parser.add_argument('uri')

    '''' 
    # 1.1 Vision features
    web_parser = subparsers.add_parser(
        'web', help=detect_web.__doc__)
    web_parser.add_argument('path')

    web_uri_parser = subparsers.add_parser(
        'web-uri',
        help=detect_web_uri.__doc__)
    web_uri_parser.add_argument('uri')

    web_geo_parser = subparsers.add_parser(
        'web-geo', help=web_entities_include_geo_results.__doc__)
    web_geo_parser.add_argument('path')

    web_geo_uri_parser = subparsers.add_parser(
        'web-geo-uri',
        help=web_entities_include_geo_results_uri.__doc__)
    web_geo_uri_parser.add_argument('uri')

    crop_hints_parser = subparsers.add_parser(
        'crophints', help=detect_crop_hints.__doc__)
    crop_hints_parser.add_argument('path')

    crop_hints_uri_parser = subparsers.add_parser(
        'crophints-uri', help=detect_crop_hints_uri.__doc__)
    crop_hints_uri_parser.add_argument('uri')

    document_parser = subparsers.add_parser(
        'document', help=detect_document.__doc__)
    document_parser.add_argument('path')

    document_uri_parser = subparsers.add_parser(
        'document-uri', help=detect_document_uri.__doc__)
    document_uri_parser.add_argument('uri')

    ocr_uri_parser = subparsers.add_parser(
        'ocr-uri', help=async_detect_document.__doc__)
    ocr_uri_parser.add_argument('uri')
    ocr_uri_parser.add_argument('destination_uri')

    object_localization_parser = subparsers.add_parser(
        'object-localization', help=async_detect_document.__doc__)
    object_localization_parser.add_argument('path')

    object_localization_uri_parser = subparsers.add_parser(
        'object-localization-uri', help=async_detect_document.__doc__)
    object_localization_uri_parser.add_argument('uri')
'''
    args = parser.parse_args()

    if 'uri' in args.command:
        run_uri(args)
    else:
        run_local(args)