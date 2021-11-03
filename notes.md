## Models:
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
- Add Subject
- View Subject
- Add Subtopic
- View Subtopic (Include grade)
- Table View:
  - grades
  - subjects
  - subtopics
- JSON View