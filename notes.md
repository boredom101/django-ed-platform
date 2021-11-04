## Models:
Maybe make a base model with name, and inherit it for the other models?
- EducationLevel
  - name: CharField
- Grade
  - name: CharField
  - level: ForeignKey (EducationLevel)
- Subject
  - name: CharField
  - grades: ManyToManyField (Grade)
- Subtopic
  - name: CharField
  - subjects: ManyToManyField (Subject)

## Views:
(Use the built-in support for form, single views and table views) (And create view)
- Add Subject
- View Subject
- Add Subtopic
- View Subtopic (Include grade, this would require to access a property of a property)
- Table View:
  - grades
  - subjects
  - subtopics
- JSON View (What is the best way to do this?) (There is a JsonResponse object we can use.)

## Blocks

### Block 1 (Done):
Implement models

I used an abstract base class containing the name field and a `__str__` method, and the other classes inherited from it. (`EducationLevel` is empty but it is still important to tell it apart from other models for relationship purposes)

### Block 2 (Done):
Create views and corresponding url paths

Added views, though there is a bit of repitition.
Also there is no support for secondarySubjects.
And I am not sure about the ManyToMany support.

### Block 3 (Done):
Add templates

Mistake: I forgot the `method` attribute of the `form` tag.

### Block 4:
Configure admin

### Block 5:
Test