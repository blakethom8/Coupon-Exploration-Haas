import dash
from dash import Input, Output, State, callback, dcc, html, dash_table

from database import db, Image
import boto3
from botocore.exceptions import ClientError




dash.register_page(__name__, name='Saved Graphs')


def create_presigned_url(bucket_name, object_name, expiration=3600):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    # Generate a presigned URL for the S3 object
    s3 = boto3.client('s3',
                      aws_access_key_id='AKIA5YBQKQYJBKCQPKGE',
                      aws_secret_access_key='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',
                      region_name='us-west-2'
                      )
    try:
        response = s3.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response

layout = html.Div([
    html.Button('Refresh Images', id='refresh-button'),
    html.Br(),
    html.Div(id='saved-images'),
    html.Br(),
    html.Br(),

])


@callback(
    Output('saved-images', 'children'),
    Input('refresh-button', 'n_clicks'),
)
def update_saved_images(n):
    if n is None:
        return []
    current_user = 1111
    images = Image.query.filter_by(user_id=current_user).all()
    img_elements = []
    for img in images:
        signed_url = create_presigned_url('coupondashboardhaasdatabase', img.path)
        img_element = html.Img(src=signed_url)
        img_elements.append(img_element)
    return img_elements
