# HTML Review

Review the concepts below to prepare for the upcoming prep exam.

---

## 🟦 HTML Basics

- **Role of HTML:** Defines the structure of a webpage.
- **HTML Elements:** Created with opening & closing tags (e.g. `<h1>`, `<p>`).
- **HTML Structure:** Includes `<head>` (metadata) and `<body>` (content).
- **Common Elements:** Headings, paragraphs, div containers.
- **`div` Element:** Generic container with no semantic meaning.
- **Void Elements:** No closing tag (e.g. `<img>`).
- **Attributes:** Add metadata or behavior to elements.

---

## 🟩 Identifiers and Grouping

- **ID:** Unique identifier for one element.
- **Class:** Groups elements for styling or behavior.

---

## 🔠 Special Characters & Linking

- **HTML Entities:** `&amp;`, `&lt;`, `&gt;`, etc.
- **`<link>`:** Attach external CSS.
- **`<script>`:** Attach external JavaScript.

---

## 📄 Boilerplate & Encoding

- **HTML Boilerplate:** DOCTYPE, `<html>`, `<head>`, `<body>`.
- **UTF-8 Encoding:** Ensures characters display correctly.

---

## 🔍 SEO & Social Sharing

- **Meta Description:** Short summary for search engines.
- **Open Graph Tags:** Improve preview content on social platforms.

---

## 🖼️ Media Elements & Optimization

- **Replaced Elements:** Images, videos, iframes.
- **Optimization:** Resize, compress, use correct format.
- **Image Licenses:** Know usage rights.
- **SVGs:** Scalable vector graphics for sharp visuals.

---

## 🎬 Multimedia Integration

- **`<audio>` & `<video>`** for media.
- **`<iframe>`** for embedding external content.

---

## 📁 Paths & Link Behavior

- **Target Attributes:** Ex. `_blank` opens in new tab.
- **Absolute vs. Relative Paths**
- **Path Syntax:** `/`, `./`, `../`
- **Link States:** hover, active, visited.

---

## 🧱 Importance of Semantic HTML

### Structural Elements

- Use heading levels `<h1>` to `<h6>` logically.
- Avoid deprecated presentational tags: `<center>`, `<font>`, etc.

### Semantic Structure

- `<header>`
- `<nav>`
- `<article>`
- `<aside>`
- `<section>`
- `<footer>`

### Semantic Inline Elements

- **`<em>`** – emphasis
- **`<i>`** – idiomatic / alternative voice
- **`<strong>`** – strong importance
- **`<b>`** – attention
- **`<dl> <dt> <dd>`** – description lists
- **`<blockquote>`** – long quotations
- **`<q>`** – inline quotation
- **`<abbr>`** – abbreviation
- **`<address>`** – contact info
- **`<time>`** – date/time
- **`<sup>` / `<sub>`** – superscript/subscript
- **`<code>`** – inline code
- **`<u>`** – annotation
- **`<ruby>`** – ruby annotations
- **`<s>`** – strikethrough

---

## 📝 HTML Forms & Attributes

### Form Structure

- `<form>` wraps the inputs.
- **action:** where data is sent.
- **method:** GET or POST.

### Input Types

Common types:  
`text`, `email`, `password`, `radio`, `checkbox`, `number`, `date`

### Input Attributes

- **placeholder**
- **value**
- **name**
- **size**
- **min / max**
- **minlength / maxlength**
- **required**
- **disabled**
- **readonly**

### Labels

- **Implicit:** Wrap input inside `<label>`
- **Explicit:** Use `for` + matching input `id`

### Buttons

- `<button type="button">`
- `<button type="submit">`
- `<button type="reset">`

### Fieldsets & Legends

Used to group related inputs:

```html
<fieldset>
  <legend>Example Group</legend>
  ...
</fieldset>
```
