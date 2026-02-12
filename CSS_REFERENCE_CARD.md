# Quick CSS Reference Card

## Color Palette
```
Primary:    #0066cc (Blue)
Secondary:  #ff6b6b (Red)
Accent:     #00d4ff (Cyan)
Dark:       #0f1419 (Navy)
Light:      #f5f7fa (Off-White)
Gray:       #6c757d (Medium)
Success:    #10b981 (Green)
Danger:     #ef4444 (Red)
```

## Typography
```
Headings:   font-weight: 700-800, letter-spacing: -0.5px
Subheadings: font-weight: 600-700
Body:       font-weight: 400-500, line-height: 1.7
Small:      font-weight: 600, font-size: 13-14px
```

## Shadows
```
Light:   0 10px 40px rgba(0, 0, 0, 0.1)
Medium:  0 20px 60px rgba(0, 0, 0, 0.15)
Heavy:   0 40px 80px rgba(0, 0, 0, 0.2)
```

## Common Gradients
```
Blue Primary:    linear-gradient(135deg, #0066cc 0%, #004399 100%)
Red Secondary:   linear-gradient(135deg, #ff6b6b 0%, #ff3333 100%)
Dark Background: linear-gradient(135deg, #0f1419 0%, #0a0d12 100%)
```

## Spacing System
```
xs: 5px     sm: 10px    md: 20px    lg: 30px
xl: 40px    2xl: 60px   3xl: 80px   4xl: 100px
```

## Border Radius
```
Regular: 12px
Small:   8px
Large:   16px
Pill:    9999px
```

## Quick Classes

### Text
```
.gradient-text        { gradient text effect }
.text-primary        { color: #0066cc }
.text-secondary      { color: #ff6b6b }
.text-gray           { color: #6c757d }
```

### Sizing
```
.shadow-sm           { light shadow }
.shadow-md           { medium shadow }
.shadow-lg           { heavy shadow }
.shadow-xl           { extra heavy shadow }
```

### States
```
.loading             { pulse animation }
.disabled            { opacity: 0.5 }
.active              { color: primary }
```

## Responsive Breakpoints
```
Mobile:  < 480px
Tablet:  480px - 768px
Desktop: > 768px
```

## Animation Durations
```
Fast:      0.3s
Normal:    0.4s
Slow:      0.6s
Slower:    0.8s
Very Slow: 1s+
```

## Z-Index Scale
```
Dropdown:   100
Modal:      1000
Tooltip:    1100
Notification: 1200
```

## Common Hover Effects
```
Scale:     transform: scale(1.05)
Lift:      transform: translateY(-5px)
Brighten:  filter: brightness(1.1)
Shadow:    box-shadow: [larger-shadow]
Color:     color: [new-color]
```

## Icons
```
Float:     animation: float 3s ease-in-out infinite
Bounce:    animation: bounce 1s ease-in-out infinite
Spin:      animation: spin 2s linear infinite
Pulse:     animation: pulse 2s ease-in-out infinite
```

## Useful Selectors
```
[type="text"]        /* Text inputs */
[type="button"]      /* Buttons */
:focus               /* Focus state */
:hover               /* Hover state */
:disabled            /* Disabled state */
::placeholder        /* Placeholder text */
::before/:after      /* Pseudo-elements */
```

## Media Queries
```
/* Mobile First */
@media (min-width: 480px) { }
@media (min-width: 768px) { }
@media (min-width: 1024px) { }

/* Or max-width */
@media (max-width: 480px) { }
@media (max-width: 768px) { }
```

## CSS Variables
```
:root {
    --primary-color: #0066cc;
    --secondary-color: #ff6b6b;
    --accent-color: #00d4ff;
    --dark-color: #0f1419;
    --light-color: #f5f7fa;
    --gray-color: #6c757d;
    --success-color: #10b981;
    --danger-color: #ef4444;
    --info-color: #3b82f6;
    --radius: 12px;
    --shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 20px 60px rgba(0, 0, 0, 0.15);
    --transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
```

## Useful Utilities
```
/* Smooth Transitions */
transition: var(--transition);

/* Smooth Colors */
color: var(--primary-color);
background: var(--light-color);

/* Smooth Shadows */
box-shadow: var(--shadow);

/* Rounded Corners */
border-radius: var(--radius);

/* Flex Center */
display: flex;
align-items: center;
justify-content: center;

/* Grid System */
display: grid;
grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
gap: 30px;
```

## Animation Keyframes
```
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes slideInLeft {
    from { opacity: 0; transform: translateX(-30px); }
    to { opacity: 1; transform: translateX(0); }
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.7; }
}
```

## Image Optimization URLs
```
Width:    ?w=400          /* Set width */
Quality:  ?q=80           /* 1-100 scale */
Crop:     ?crop=entropy   /* Smart crop */
Full URL: ?w=400&q=80&crop=entropy
```

## Common Patterns

### Card Styling
```css
background: white;
padding: 30px;
border-radius: 12px;
box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
transition: all 0.4s ease;
```

### Button Styling
```css
padding: 14px 32px;
border: none;
border-radius: 12px;
font-weight: 700;
cursor: pointer;
transition: all 0.4s ease;
background: linear-gradient(135deg, #0066cc 0%, #004399 100%);
color: white;
```

### Input Styling
```css
padding: 14px 16px;
border: 2px solid #e0e0e0;
border-radius: 12px;
font-size: 15px;
background-color: #f8f9fa;
transition: all 0.3s ease;
```

### Hero Section
```css
background: linear-gradient(135deg, rgba(0, 102, 204, 0.85) 0%, rgba(0, 68, 153, 0.85) 100%), url('image-url');
background-size: cover;
background-position: center;
min-height: 600px;
color: white;
display: flex;
align-items: center;
justify-content: center;
```

---

Print this reference for quick access during development!
