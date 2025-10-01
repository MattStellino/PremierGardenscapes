# 🎨 Landscaping Card Design System

## Overview
A modern, nature-inspired card component system designed specifically for landscaping websites. Built with CSS variables, responsive design, and accessibility in mind.

## 🚀 Features

### Design Principles
- **Nature-inspired colors**: Forest greens, earth browns, sand tones
- **Clean & airy**: Generous spacing and modern typography
- **Responsive**: Mobile-first design with Bootstrap grid integration
- **Accessible**: High contrast, focus states, reduced motion support

### Card Variants
- **Default**: Clean white cards with green accents
- **Service**: Special styling for service offerings
- **Gallery**: Optimized for image-heavy content
- **Brown**: Earth-tone variant for hardscaping sections
- **Compact**: Smaller version for testimonials

## 📁 File Structure

```
static/main/css/
├── cards.css          # New card design system
├── styles.css         # Legacy styles (cleaned up)
└── base.html          # Imports cards.css
```

## 🎯 Usage Examples

### Basic Service Card
```html
<div class="col-12 col-sm-6 col-lg-4">
  <div class="card-landscape service h-100">
    <div class="card-media">
      <img src="{% static 'main/images/service.jpg' %}" 
           alt="Service Name" 
           loading="lazy">
    </div>
    <div class="card-body">
      <div class="card-subtitle">Category</div>
      <h4 class="card-title">Service Title</h4>
      <p class="card-text">Service description goes here.</p>
      <div class="card-chips">
        <span class="card-chip">Free Estimate</span>
        <span class="card-chip">Seasonal</span>
      </div>
    </div>
    <div class="card-footer">
      <div class="card-actions">
        <a href="#contact" class="card-btn">
          <i class="fas fa-phone"></i>
          Get Quote
        </a>
      </div>
    </div>
  </div>
</div>
```

### Brown Variant (Hardscaping)
```html
<div class="card-landscape brown h-100">
  <!-- Same structure, different color scheme -->
</div>
```

### Compact Variant
```html
<div class="card-landscape compact h-100">
  <!-- Smaller padding and typography -->
</div>
```

## 🎨 CSS Variables

### Color Palette
```css
:root {
  --ls-primary: #2d5a4a;        /* Deep forest green */
  --ls-primary-light: #4a7c59;  /* Medium green */
  --ls-primary-lighter: #7a9b8a; /* Light sage */
  --ls-accent: #8b4513;         /* Rich earth brown */
  --ls-earth: #8b7355;          /* Natural brown */
  --ls-sand: #f4e4c1;           /* Light sand */
  --ls-cream: #faf8f3;          /* Off-white cream */
}
```

### Spacing & Shadows
```css
:root {
  --ls-radius: 16px;            /* Base border radius */
  --ls-radius-lg: 20px;         /* Large border radius */
  --ls-spacing: 24px;           /* Standard padding */
  --ls-shadow: 0 4px 16px rgba(45, 90, 74, 0.12);
  --ls-shadow-hover: 0 12px 40px rgba(45, 90, 74, 0.25);
}
```

## 📱 Responsive Design

### Grid System
- **Mobile**: `col-12` (full width)
- **Small**: `col-sm-6` (2 columns)
- **Large**: `col-lg-4` (3 columns)

### Breakpoints
- **Mobile**: `< 576px` - Stacked layout, smaller text
- **Tablet**: `576px - 768px` - 2-column layout
- **Desktop**: `> 768px` - 3-column layout

## ♿ Accessibility Features

### Focus States
- Clear focus outlines for keyboard navigation
- High contrast mode support
- Reduced motion preferences respected

### Screen Reader Support
- Semantic HTML structure
- Proper alt text for images
- ARIA labels where needed

## 🔧 Customization

### Adding New Variants
```css
.card-landscape.custom-variant {
  background: var(--your-custom-color);
  border-left: 4px solid var(--your-accent);
}

.card-landscape.custom-variant .card-title {
  color: var(--your-text-color);
}
```

### Modifying Colors
```css
:root {
  --ls-primary: #your-green;
  --ls-accent: #your-brown;
  --ls-cream: #your-off-white;
}
```

## 🧹 Maintenance

### What Was Removed
- Old `.service-card` styles
- Redundant shadow definitions
- Unused icon styles
- Duplicate card styling

### What Was Kept
- Legacy card styles for compatibility
- Base typography and spacing
- Hero section styling
- Form and button styles

## 🚀 Performance

### Optimizations
- CSS variables for consistent theming
- Efficient selectors and minimal nesting
- Lazy loading for images
- Reduced CSS bundle size

### Browser Support
- Modern browsers (Chrome 60+, Firefox 55+, Safari 12+)
- CSS Grid and Flexbox support
- CSS Custom Properties support

## 📋 Implementation Checklist

- [x] Create `cards.css` with design system
- [x] Import in `base.html`
- [x] Update service cards in `home.html`
- [x] Clean up old styles in `styles.css`
- [x] Test responsive behavior
- [x] Verify accessibility features
- [x] Document usage patterns

## 🎯 Next Steps

1. **Add more card variants** for different content types
2. **Create image placeholders** for missing service images
3. **Add card animations** for enhanced interactivity
4. **Implement card filtering** for service categories
5. **Add card search** functionality

## 🔍 Troubleshooting

### Common Issues
- **Cards not styling**: Check if `cards.css` is imported
- **Images not loading**: Verify image paths and static file collection
- **Responsive issues**: Ensure Bootstrap classes are correct
- **Hover effects not working**: Check for CSS conflicts

### Debug Mode
Add this to your CSS for debugging:
```css
.card-landscape {
  border: 2px solid red !important;
}
```

---

**Created**: 2024
**Framework**: Django + Bootstrap 5
**Design**: Nature-inspired, modern landscaping aesthetic
**Status**: ✅ Complete and ready for production
