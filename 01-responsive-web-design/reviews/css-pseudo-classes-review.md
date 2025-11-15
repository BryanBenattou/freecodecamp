# CSS Pseudo-classes Review

Review the concepts below to prepare for the upcoming prep exam.

---

## 🟦 User Action Pseudo-classes

Pseudo-classes change the appearance of elements based on user interactions.

- **`:active`** – Styles an element while it's being clicked.
- **`:hover`** – Styles an element when the pointer is over it.
- **`:focus`** – Styles an element when it receives keyboard or click focus.
- **`:focus-within`** – Styles an element when it _or any of its descendants_ has focus.

---

## 🟩 Input Pseudo-classes

Used to target inputs based on validation, requirement, or browser state.

- **`:enabled`** – Selects interactive inputs/buttons.
- **`:disabled`** – Selects disabled inputs.
- **`:checked`** – Matches checked checkboxes and radio buttons.
- **`:valid`** – Field meets validation rules.
- **`:invalid`** – Field does _not_ meet validation rules.
- **`:in-range`** / **`:out-of-range`** – Applies to numeric inputs based on allowed range.
- **`:required`** – Input has a `required` attribute.
- **`:optional`** – Input is optional.
- **`:autofill`** – Input is automatically filled by the browser.

---

## 🔗 Location Pseudo-classes

Used for styling links and fragment-targeted elements.

- **`:any-link`** – Matches any link with `href`.
- **`:link`** – Unvisited links.
- **`:local-link`** – Links pointing to the same page.
- **`:visited`** – Previously visited links.
- **`:target`** – Element targeted by a URL `#fragment`.
- **`:target-within`** – Element or descendant is the fragment target.

---

## 🌳 Tree-Structural Pseudo-classes

Targets elements based on their position in the DOM tree.

- **`:root`** – Selects the document root (`html`).
- **`:empty`** – Elements with no children or text.
- **`:nth-child(n)`** – Selects element by index.
- **`:nth-last-child(n)`** – Index from the end.
- **`:first-child`** – First child of its parent.
- **`:last-child`** – Last child of its parent.
- **`:only-child`** – Single child of its parent.
- **`:first-of-type`** – First of its type.
- **`:last-of-type`** – Last of its type.
- **`:nth-of-type(n)`** – Index within its type.
- **`:only-of-type`** – Only element of its type.

---

## 🧩 Functional Pseudo-classes

These accept arguments and allow more complex selections.

### **`:is()`**

Matches if any selector in the list matches.

```css
p:is(.example, .this-works-too) {
  color: red;
}
```

### HTML Example

```html
<p class="example">This text will change color.</p>
<p>This text will not change color.</p>
<p>This text will not change color.</p>
<p class="this-works-too">This text will change color.</p>
```

### **`:where()`**

Same as `:is()` but **specificity = 0**.

```css
:where(h1, h2, h3) {
  margin: 0;
  padding: 0;
}
```

### **`:has()`**

A powerful _parent selector_.

```css
article:has(h2) {
  border: 2px solid hotpink;
}
```

### **`:not()`**

Selects elements that do _not_ match a selector.

```css
p:not(.example) {
  color: blue;
}
```

---

## 🎨 Pseudo-elements

Pseudo-elements style specific parts of an element.

- **`::before`** – Inserts content before an element.
- **`::after`** – Inserts content after an element.
- **`::first-letter`** – Styles the first letter.
- **`::marker`** – Styles list bullets or numbers.

---
