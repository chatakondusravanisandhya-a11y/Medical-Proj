# Adding AI Pictures for Doctors and Departments

## Overview
The Hospital Management System now supports uploading images for doctors and departments. You can add AI-generated pictures through multiple methods.

## Method 1: Using the Management Command (Recommended)

Run the management command to automatically add placeholder or AI images:

```bash
# Add images for all doctors and departments with placeholders
python manage.py add_ai_images --type both --service placeholder

# Add images for only doctors
python manage.py add_ai_images --type doctors --service placeholder

# Add images for only departments
python manage.py add_ai_images --type departments --service placeholder

# Use Unsplash for more realistic medical images
python manage.py add_ai_images --type both --service unsplash
```

### Available Services:
- **placeholder**: Quick UI-generated avatars and placeholder images
- **unsplash**: High-quality medical and professional photos from Unsplash
- **pexels**: (Instructions for integration with Pexels API)

## Method 2: Upload Through Django Admin Panel

1. Go to `/admin/`
2. Navigate to **Departments** or **Doctors**
3. Click on an existing entry to edit
4. Scroll down to the **Image** field
5. Upload an image or paste an image URL
6. Click **Save**

## Method 3: Using AI Image Generation Services

### Integration with OpenAI DALL-E

To generate truly AI-created images:

```python
import openai
from django.core.files.base import ContentFile
from hospital_system.models import Doctor

openai.api_key = "your-api-key"

def generate_doctor_image(doctor):
    response = openai.Image.create(
        prompt=f"A professional portrait of a {doctor.specialization} doctor named {doctor.name}",
        n=1,
        size="256x256"
    )
    image_url = response['data'][0]['url']
    
    # Download and save
    import requests
    img = requests.get(image_url).content
    doctor.image.save(f'{doctor.name}.png', ContentFile(img), save=True)
```

### Integration with Stability AI

```python
import requests
from django.core.files.base import ContentFile
from hospital_system.models import Department

def generate_department_image(dept):
    response = requests.post(
        "https://api.stability.ai/v1/generation/stable-diffusion-v1-6/text-to-image",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {STABILITY_AI_KEY}"
        },
        json={
            "text_prompts": [{"text": f"A modern hospital {dept.name} department, professional, clean"}],
            "cfg_scale": 7,
            "height": 512,
            "width": 512,
            "samples": 1,
            "steps": 30,
        }
    )
    
    # Process response...
```

## Method 4: Batch Upload via CSV

Create a CSV file with the following format:

```csv
type,id,image_url
doctor,1,https://example.com/doctor1.jpg
doctor,2,https://example.com/doctor2.jpg
department,1,https://example.com/cardiology.jpg
```

Then run a custom script to process it.

## Image Requirements

- **Format**: JPG, PNG, or WebP
- **Doctor Images**: At least 400x400px (recommended: 600x600px)
- **Department Images**: At least 800x600px (recommended: 1200x800px)
- **File Size**: Less than 5MB recommended

## Supported Image Sources

### Free Services
- **UI Avatars**: https://ui-avatars.com (Professional avatars)
- **Unsplash**: https://unsplash.com (High-quality photos)
- **Pexels**: https://pexels.com (Free stock photos)
- **Placeholder**: https://via.placeholder.com (Quick placeholders)

### Paid AI Services
- **OpenAI DALL-E**: Text to image generation
- **Stability AI**: Advanced image generation
- **Midjourney**: Creative image generation (via API)
- **Adobe Firefly**: Professional image generation

## Troubleshooting

### Images not showing on website
1. Run `python manage.py collectstatic` to collect static files
2. Check that media directories have proper permissions
3. Verify image file paths in admin panel

### Slow performance with large images
1. Consider optimizing images before upload
2. Use a CDN for image delivery
3. Set up image caching

### Failed command execution
1. Ensure `requests` library is installed: `pip install requests`
2. Check internet connection for downloading images
3. Verify API keys if using AI services

## Adding Images Manually (Step by Step)

1. **For Doctors**:
   - Open Django admin
   - Click on "Doctors"
   - Click the doctor's name
   - Scroll to "Image"
   - Upload a professional headshot
   - Save

2. **For Departments**:
   - Open Django admin
   - Click on "Departments"
   - Click the department name
   - Scroll to "Image"
   - Upload a department photo
   - Save

## Preview Images in Admin

The admin panel now shows:
- **Doctor images**: 100x100px preview
- **Department images**: 50x50px preview in list view

This helps you verify images before they appear on the website.

---

**Need Help?** Contact the development team or consult the Django documentation on file uploads.
