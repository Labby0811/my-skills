---
name: commented-code
description: Code documentation and naming rules layered on top of ponytail. Use whenever writing or editing code in any language. Always active via SessionStart hook.
---

# Commented code

## Priority
Ponytail stays the main rule set: scope, smallest solution, dependencies,
tests, shortcuts, shortest diff. This skill never changes WHICH code gets
written. It only changes HOW that code is documented and named.

## Override
It replaces ONLY this ponytail rule:
  "Comment only the why the code cannot show, in one line."
Every other ponytail rule stays unchanged.

## Rules
1. Language: all comments and docstrings in English.
2. Function docs: every function, method and class gets a doc comment,
   including small private helpers. Format:
   - one short sentence that says what it does;
   - then Google-style sections: Args, Returns, Raises.
     Omit a section that is empty.
   - Python uses """ docstrings. Other languages use their native doc syntax:
     /** */ or /// in C++, JSDoc in JS/TS, # comment block in bash, etc.
3. Block comments: each logical block (lines that do one step together)
   gets a one-line comment above it saying what happens. Use a few words.
4. Complex logic (math, geometry, non-obvious algorithm, workaround)
   gets a short comment with what it does and why. Max 2-3 lines.
5. Comments stay short. They follow the shortest-diff spirit too:
   explain what happens in a few words, never a paragraph.
6. Names: descriptive and intuitive for variables, functions and classes.
   Never use invented abbreviations. Never use single letters,
   except loop indices and standard math notation that matches a formula.
7. Units: physical quantities carry the unit in the name
   (distance_m, yaw_rad, angle_deg, timeout_s, offset_mm).
   Docstring Args and Returns also state the unit.
8. Existing code: when you modify a function that has no docs or comments,
   add them to that function. Do not touch functions outside the change.
9. Comments do NOT count in ponytail's "shortest diff" measure.

## Never
- Comments that repeat the line (x += 1  # increment x).
- Decorative or banner comments.
- Deleting or shortening existing comments you were not asked to change.

## Example (Python)
```python
def fit_plane(points_m):
    """Fit a plane to 3D points with least squares.

    Args:
        points_m: (N, 3) array of points, in meters.

    Returns:
        (normal, offset_m): unit normal vector and plane offset in meters.
    """
    # Center points so the SVD finds the direction of least variance
    centroid_m = points_m.mean(axis=0)
    _, _, vh = np.linalg.svd(points_m - centroid_m)
    normal = vh[-1]
    return normal, normal @ centroid_m
```
