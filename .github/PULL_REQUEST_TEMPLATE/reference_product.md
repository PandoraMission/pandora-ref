## Summary

Describe what this PR updates or changes. Include which reference products are affected and why. Discuss the providence of the data, link to any code that has been used to generate the product if appropriate.

---

## Files Updated

List all reference files that were added, removed, or modified.

| File path | Change type | Old version | New version |
|------------|--------------|--------------|--------------|
| `src/pandoraref/data/NIRDA/flat.fits` | updated | 1.2.4 | 1.2.5 |
| `src/pandoraref/data/NIRDA/badpix.fits` | updated | 0.2.1 | 1.0.0 |

---

## Verification

- [ ] Verified file format matches previous version (if not state why in summary)
- [ ] Verified headers, extensions, and metadata are consistent (if not state why in summary)
- [ ] Verified new file(s) has new version number  
- [ ] Verified filenames follow convention  
- [ ] Verified new files do not greatly increase file size (discuss below if they do increase file size.)
- [ ] Verified `pyproject.toml` version incremented correctly  
- [ ] Verified CHANGELOG updated  

---

## Versioning

What kind of version bump does this require?

- [ ] **Patch** — Data changed, structure unchanged  
- [ ] **Minor** — Structure changed (added/removed headers or extensions)  
- [ ] **Major** — Added or removed entire reference products  

---

## Additional Notes

Include any details reviewers should know (e.g. source of new calibration data, expected downstream impact).

---

## Reviewer Guidance

Reviewers should confirm:

- All checklist items completed  
- Versioning rule followed  
- File diffs correspond to legitimate reference updates  
- README and CHANGELOG reflect the changes
