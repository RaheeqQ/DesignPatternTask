# DesignPatternTask
```python
# 🎯Problem 10 — Undo / Redo & Macros

Menu items call document methods directly; no command history exists.

## Requirements
• Wrap every user action in a Command object with execute() and undo().
• Maintain a history stack for multi‐level undo/redo.
• Allow grouping multiple commands into a macro. 

## Ugly Starter Code
def type_text(doc, text):
    doc += text
    return doc
def delete_text(doc):
    return doc[:-1]
document = ""
document = type_text(document, "Hello")
document = delete_text(document)
```
