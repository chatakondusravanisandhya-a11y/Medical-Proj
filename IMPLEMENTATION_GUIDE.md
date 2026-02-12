# Implementation Guide - Premium Design Features

## Quick Reference

### 1. Color Variables (Update in CSS :root)
```css
--primary-color: #0066cc;      /* Professional Blue */
--secondary-color: #ff6b6b;    /* Modern Red */
--accent-color: #00d4ff;       /* Cyan - Tech */
--dark-color: #0f1419;         /* Deep Navy */
--light-color: #f5f7fa;        /* Off White */
--gray-color: #6c757d;         /* Medium Gray */
```

### 2. Premium Reusable Classes

```html
<!-- Shadow Classes -->
<div class="shadow-sm">Light shadow</div>
<div class="shadow-md">Medium shadow</div>
<div class="shadow-lg">Large shadow</div>
<div class="shadow-xl">Extra large shadow</div>

<!-- Badge Classes -->
<span class="badge badge-primary">Primary</span>
<span class="badge badge-success">Success</span>
<span class="badge badge-secondary">Secondary</span>

<!-- Gradient Text -->
<h2 class="gradient-text">Gradient Text Effect</h2>

<!-- Loading State -->
<div class="loading">Loading animation</div>
```

### 3. Image Implementation

```html
<!-- Hero Image -->
<section class="hero" style="background-image: linear-gradient(135deg, rgba(0, 102, 204, 0.85) 0%, rgba(0, 68, 153, 0.85) 100%), url('https://images.unsplash.com/photo-1576091160550-112173f7f869?w=1200&h=600&q=85');">

<!-- Doctor Image with Fallback -->
<img src="https://images.unsplash.com/photo-1612349317150-e577a8a40aa0?w=400&q=85" alt="Doctor Name" loading="lazy">

<!-- Department Card with Image -->
<div class="dept-header" style="background: linear-gradient(135deg, rgba(0, 102, 204, 0.8) 0%, rgba(0, 68, 153, 0.8) 100%), url('{{ image_url }}'); background-size: cover; background-position: center; background-blend-mode: overlay;">
```

### 4. Common Image URLs Reference

```
Heroes/Backgrounds:
- Hospital Corridor: https://images.unsplash.com/photo-1519494026892-80bbd2651601?w=1200&q=80
- Medical Team: https://images.unsplash.com/photo-1576091160550-112173f7f869?w=1200&q=80
- Doctor Consultation: https://images.unsplash.com/photo-1631217314831-4ad4467a8cb5?w=1200&q=80

Doctors:
- Male Doctor: https://images.unsplash.com/photo-1537537984623-2b5e0d0c5b2e?w=400&q=80
- Female Doctor: https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400&q=80
- Professional: https://images.unsplash.com/photo-1612349317150-e577a8a40aa0?w=400&q=80

Departments:
- General: https://images.unsplash.com/photo-1576091160550-2173f7f869e0?w=200&q=80
- Cardiology: https://images.unsplash.com/photo-1579154204601-01d82b1d9b1f?w=200&q=80
- Lab: https://images.unsplash.com/photo-1576091160550-112173f7f869?w=200&q=80

Services:
- Checkup: https://images.unsplash.com/photo-1576686213496-bb876674b726?w=400&q=80
- Emergency: https://images.unsplash.com/photo-1576091160499-112eb8391fcb?w=400&q=80
- Lab: https://images.unsplash.com/photo-1530836369250-ef72a3f26da8?w=400&q=80
```

### 5. Animation Classes

```html
<!-- Fade In Animation -->
<div style="animation: fadeIn 0.6s ease-out;"></div>

<!-- Slide Up Animation (with delay) -->
<div class="feature-card" style="animation-delay: 0.2s;"></div>

<!-- Float Animation -->
<i class="fas fa-icon" style="animation: float 3s ease-in-out infinite;"></i>

<!-- Pulse Loading -->
<div class="loading"></div>
```

### 6. Button Styles

```html
<!-- Primary Button -->
<a href="#" class="btn btn-primary">Primary Button</a>

<!-- Secondary Button -->
<a href="#" class="btn btn-secondary">Secondary Button</a>

<!-- Large Button -->
<a href="#" class="btn btn-primary btn-lg">Large Button</a>

<!-- Full Width -->
<a href="#" class="btn btn-primary" style="width: 100%; display: block;">Full Width</a>
```

### 7. Form Styling

```html
<div class="form-group">
    <label for="name">Name</label>
    <input type="text" id="name" placeholder="Enter your name" required>
</div>

<!-- Form with Success State -->
<div class="form-group success">
    <label for="email">Email</label>
    <input type="email" id="email" required>
</div>

<!-- Form with Error State -->
<div class="form-group error">
    <label for="phone">Phone</label>
    <input type="tel" id="phone" required>
</div>
```

### 8. Card Styling

```html
<!-- Feature Card -->
<div class="feature-card">
    <i class="fas fa-icon"></i>
    <h3>Title</h3>
    <p>Description</p>
</div>

<!-- Doctor Card -->
<div class="doctor-profile-card">
    <div class="doctor-image-container">
        <img src="..." alt="...">
        <span class="availability-badge available">Available</span>
    </div>
    <div class="doctor-info">
        <h3>Dr. Name</h3>
        <p class="specialty">Specialty</p>
        <p class="fee"><strong>Fee:</strong> ₹Amount</p>
    </div>
</div>

<!-- Department Card -->
<div class="dept-card">
    <div class="dept-icon">
        <img src="..." alt="...">
    </div>
    <h3>Department Name</h3>
    <p>Description</p>
</div>
```

### 9. Section Styling

```html
<!-- Hero Section -->
<section class="hero" style="background-image: ..."></section>

<!-- Section with White Background -->
<section style="background: white; padding: 100px 20px;">

<!-- Section with Light Gray Background -->
<section style="background: #f5f7fa; padding: 100px 20px;">

<!-- CTA Section -->
<section class="cta-section">
```

### 10. Responsive Images

```html
<!-- Basic Image -->
<img src="https://images.unsplash.com/...?w=400&q=80" alt="Description">

<!-- Image with Loading -->
<img src="..." alt="..." loading="lazy">

<!-- Image Container -->
<div class="image-container">
    <img src="..." alt="...">
    <div class="overlay"></div>
</div>
```

### 11. Typography Classes

```html
<!-- Gradient Text -->
<h2 class="gradient-text">Gradient Heading</h2>

<!-- Normal Heading -->
<h2 style="font-size: 42px; font-weight: 800; letter-spacing: -0.5px;">Premium Heading</h2>

<!-- Subtitle -->
<p style="font-size: 18px; font-weight: 300; letter-spacing: 0.3px;">Modern Subtitle</p>
```

### 12. Icon Styling

```html
<!-- Floating Icon -->
<i class="fas fa-icon" style="font-size: 48px; color: #0066cc; animation: float 3s ease-in-out infinite;"></i>

<!-- With Hover Effect -->
<i class="fas fa-icon"></i> <!-- Will float on hover via CSS -->

<!-- Icon in Button -->
<a href="#" class="btn btn-primary">
    <i class="fas fa-icon"></i> Button With Icon
</a>
```

## Pro Tips

1. **Always use loading="lazy"** for images to improve performance
2. **Use ?w= and ?q=** parameters in Unsplash URLs for optimization
3. **Add alt text** to all images for accessibility
4. **Test animations** on mobile devices for performance
5. **Use prefers-reduced-motion** for users with motion sensitivity
6. **Optimize images** to under 100KB where possible
7. **Use proper color contrast** for better readability
8. **Mobile-first approach** for responsive design

## Common Patterns

### Hero with Image and Text Overlay
```html
<section class="hero" style="background: linear-gradient(135deg, rgba(0, 102, 204, 0.85) 0%, rgba(0, 68, 153, 0.85) 100%), url('...'); background-size: cover; background-position: center;">
    <h1>Your Title</h1>
    <p>Your Subtitle</p>
</section>
```

### Card Grid
```html
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px;">
    <!-- Cards go here -->
</div>
```

### Stat Cards
```html
<div style="background: linear-gradient(135deg, #0066cc 0%, #004399 100%); color: white; padding: 40px; border-radius: 12px; text-align: center;">
    <h3 style="font-size: 40px; font-weight: 800;">15000+</h3>
    <p>Description</p>
</div>
```

---

**Remember**: Check `PREMIUM_DESIGN_GUIDE.md` for complete documentation!
