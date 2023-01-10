import functions_framework
from PIL import Image, ImageDraw, ImageSequence, ImageFont
import io

#@functions_framework.http
#def hello(request):
#    return "Hello world!!!!!"


#@functions_framework.cloud_event
#def hello_cloud_event(cloud_event):
#   print(f"Received event with ID: {cloud_event['id']} and data {cloud_event.data}")


@functions_framework.http
def main(cloud_event):
    #parse request params
    return makeVVSignature(cloud_event['name'],cloud_event['title'],cloud_event['phone'],cloud_event['addr1'],cloud_event['addr2'])

def makeVVSignature(name, title, phone='', addr1='1000 Sount Pine Island Road, Suite 600', addr2='Plantation, Florida 33324 USA', blankFname='email_sig_Blank.gif'):
    blank = Image.open(blankFname)
    book20 = ImageFont.truetype('fonts/CentraNo2-Book.ttf', 20)
    black22 = ImageFont.truetype('fonts/CentraNo2-Black.ttf', 22)
    book = ImageFont.truetype('fonts/CentraNo2-Book.ttf', 22)
    headln = ImageFont.truetype('fonts/Voyages-Headline.otf', 44)
    frames = []
    frames = ImageSequence.all_frames(blank)
    for f in frames:
        d = ImageDraw.Draw(f)
        d.text((240, 20), name, font=headln, fill=(60,16,83))
        d.text((240, 80), title, font=book, fill=(60,16,83))
        d.text((240, 110), phone, font=book20, fill=(60,16,83))
        d.text((240, 160), addr1, font=book20, fill=(60,16,83))
        d.text((240, 185), addr2, font=book20, fill=(60,16,83))
        del d
        b = io.BytesIO()
        f.save(b, format="GIF")
        f = Image.open(b)
    print(f'Saving {name}.gif...')
    frames[0].save(f'{name}.gif', save_all=True, append_images=frames[1:])
    print(f'Saving {name}.png...')
    frames[67].save(f'{name}.png', format='PNG')