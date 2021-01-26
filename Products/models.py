from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import *
from mptt.models import MPTTModel,TreeForeignKey
from django.contrib.auth.models import User
from ckeditor_uploader.fields import  RichTextUploadingField
from django.utils.text import slugify
from multiselectfield import MultiSelectField
from colorful.fields import RGBColorField
from colorfield.fields import ColorField
from Category.models import Category
from seller.models import Seller
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.safestring import mark_safe

# Create your models here.
class Product(models.Model):
    is_new = (
        ('True','True'),
        ('False','False'),
    )
    choice =  (
        ('Yes','Yes'),
        ('No','No'),
    )
    variants = (
        ('None','None'),
        ('Size','Size'),
        ('Color','Color'),
        ('Size-Color','Size-Color'),
    )
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    name = models.TextField(blank=False)
    is_product_new = models.CharField(max_length=225,blank=False,choices=is_new)
    brand = models.TextField(blank=False)
    description = RichTextUploadingField()
    slug = models.SlugField(blank=True,unique=True)
    status = models.BooleanField(default=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_topwear = models.BooleanField(default=False,blank=True)
    is_buttomwear = models.BooleanField(default=False,blank=True)
    varient = models.CharField(max_length=225,blank=False,choices=variants,default='None')
    wearable_type = models.TextField(blank=True,null=True)
    wearable_Sleeve = models.TextField(blank=True,null=True) 
    wearable_Fit =  models.TextField(blank=True,null=True)
    wearable_Fabric = models.TextField(blank=True,null=True)
    wearable_Faded = models.TextField(blank=True,null=True)
    wearable_Rise = models.TextField(blank=True,null=True)
    Distressed = models.TextField(blank=True,null=True)
    wearable_SalesPackage = models.TextField(blank=True,null=True)
    wearable_StyleCode = models.TextField(blank=True,null=True)
    wearable_NeckType = models.TextField(blank=True,null=True)
    wearable_IdealFor = models.TextField(blank=True,null=True)
    wearable_Pattern = models.TextField(blank=True,null=True)
    wearable_SuitableFor  = models.TextField(blank=True,null=True)
    wearable_SleeveType = models.TextField(blank=True,null=True)
    wearable_Reversible = models.TextField(blank=True,null=True)
    wearable_FabricCare = models.TextField(blank=True,null=True)
    wearable_OtherDetails = models.TextField(blank=True,null=True)
    is_mobiles = models.BooleanField(default=False,blank=True,null=True)
    In_The_Box = models.TextField(blank=True,null=True)
    Model_Number = models.TextField(blank=True,null=True)
    Model_Name = models.TextField(blank=True,null=True)
    Browse_Type = models.TextField(blank=True,null=True)
    SIM_Type = models.TextField(blank=True,null=True)
    Hybrid_Sim_Slot = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Touchscreen  = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    OTG_Compatible  = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Quick_Charging = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    SAR_Value = models.TextField(blank=True,null=True)
    Display_Size = models.TextField(blank=True,null=True)
    Resolution = models.TextField(blank=True,null=True)
    Resolution_Type = models.TextField(blank=True,null=True)
    gpu = models.TextField(blank=True,null=True)
    Display_Type = models.TextField(blank=True,null=True)
    Display_Color = models.TextField(blank=True,null=True)
    Other_Display_Features = models.TextField(blank=True,null=True)
    Operating_System = models.TextField(blank=True,null=True)
    Processor_Type = models.TextField(blank=True,null=True)
    Processor_Core = models.TextField(blank=True,null=True)
    Primary_Clock_Speed = models.TextField(blank=True,null=True)
    Secondary_Clock_Speed = models.TextField(blank=True,null=True)
    Operating_Frequency = models.TextField(blank=True,null=True)
    Internal_Storage = models.TextField(blank=True,null=True)
    Expandable_Storage = models.TextField(blank=True,null=True)
    Supported_Memory_Card_Type = models.TextField(blank=True,null=True)
    Memory_Card_Slot_Type = models.TextField(blank=True,null=True)
    Call_Log_Memory = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Primary_Camera_Available = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Primary_Camera = models.TextField(blank=True,null=True)
    Primary_Camera_Features = models.TextField(blank=True,null=True)
    Secondary_Camera_Available  = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Secondary_Camera = models.TextField(blank=True,null=True)
    Secondary_Camera_Features = models.TextField(blank=True,null=True)
    Flash = models.TextField(blank=True,null=True)
    HD_Recording = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Full_HD_Recording = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Video_Recording = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Video_Recording_Resolution = models.TextField(blank=True,null=True)
    Image_Editor = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Dual_Camera_Lens = models.TextField(blank=True,null=True)
    Call_Wait_Hold = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Conference_Call = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Hands_Free = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Video_Call_Support = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Call_Divert = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Phone_Book = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Call_Timer = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Speaker_Phone = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Speed_Dialing = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Network_Type = models.TextField(blank=True,null=True)
    Supported_Networks = models.TextField(blank=True,null=True)
    Internet_Connectivity = models.TextField(blank=True,null=True)
    is_3G = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Bluetooth_Support  = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Wi_Fi  = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Wi_Fi_Version  = models.TextField(blank=True,null=True)
    Wi_Fi_Hotspot = models.CharField(max_length=225,blank=True,choices=choice,null=True) 
    nfc = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Infrared =  models.CharField(max_length=225,blank=True,choices=choice,null=True)                
    Mini_HDMI_Port = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    USB_Tethering = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    USB_Connectivity = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    EDGE = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Audio_Jack = models.TextField(blank=True,null=True)
    Map_Support = models.TextField(blank=True,null=True)
    GPS_Support = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Smartphone = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Touchscreen_Type = models.TextField(blank=True,null=True)
    SIM_Size = models.TextField(blank=True,null=True)
    Graphics_PPI = models.TextField(blank=True,null=True)
    Sensors = models.TextField(blank=True,null=True)
    Ringtones_Format = models.TextField(blank=True,null=True)
    User_Interface = models.TextField(blank=True,null=True)
    Social_Networking_Phone = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Instant_Message = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Business_Phone = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Removable_Battery = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    MMS = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    SMS = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Keypad = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Voice_Input = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Predictive_Text_Input = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Other_Features = models.TextField(blank=True,null=True)
    GPS_Type = models.TextField(blank=True,null=True)
    Audio_Formats = models.TextField(blank=True,null=True)
    Video_Formats = models.TextField(blank=True,null=True)
    Battery_Capacity = models.TextField(blank=True,null=True)
    Talk_Time = models.TextField(blank=True,null=True)
    Dual_Battery = models.CharField(max_length=225,blank=True,choices=choice,null=True)
    Width = models.TextField(blank=True,null=True)
    Height = models.TextField(blank=True,null=True)
    Depth = models.TextField(blank=True,null=True)
    Weight = models.TextField(blank=True,null=True)
    Warranty_Summary = models.TextField(blank=True,null=True)
    Domestic_Warranty = models.TextField(blank=True,null=True)
    #image = CloudinaryField(
    #    "image",
    #    overwrite=True,
    #    resource_type="image",
    #    transformation={"quality": "auto:eco"},
    #    format="jpg",
    #)

    def __str__(self):
        return self.name

    ## method to create a fake table field in read only mode
    #def image_tag(self):
    #    if self.image.url is not None:
    #        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    #    else:
    #        return ""
 
    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

class Image(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_Image') 
    image = CloudinaryField(
        "image",
        overwrite=True,
        resource_type="image",
        transformation={"quality": "auto:eco"},
        format="jpg",
    )
    title = models.CharField(max_length=225,blank=True,null=True)

class Color(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10,blank=True,null=True)
    def __str__(self):
        return self.name
    
    def color_tag(self):
        if self.code is not None:
            return mark_safe('<p style="background-color:{}">Color</p>'.format(self.code))
        else:
            return ""

class Size(models.Model):
    name = models.CharField(max_length=28)
    code = models.CharField(max_length=10,blank=True,null=True)
    def __str__(self):
        return self.name

class Varient(models.Model):
    title = models.CharField(max_length=225,blank=True,null=True)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_varient') 
    image_id = models.IntegerField(default=0,blank=True,null=True)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(default=0)
    orignal_price = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    
    def image(self):
        img = Image.objects.get(id = self.image_id)
        if img.id is not None:
            varimage = img.image.url
        else:
            varimage = ""
        return varimage
    
    def image_tag(self):
        img = Image.objects.get(id = self.image_id)
        if img.id is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(img.image.url))
        else:
            return ""
    




