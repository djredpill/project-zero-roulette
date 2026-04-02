# Project Zero Roulette — UI Issues Report

**Date:** April 2, 2026
**Reviewed by:** Manus AI
**Method:** Automated screenshot capture at iPhone (393x852 @3x), iPad Landscape (1112x834 @2x), and iPad Portrait (834x1112 @2x)

---

## Summary

After systematically activating every feature and capturing 100 screenshots across three device viewports, the following observations were noted. Overall, the application renders well across all tested configurations.

## Issues Found

### No Critical Issues
All modals, dialogs, and reports display fully and are not cut off in any of the three tested viewports. All buttons are visible and accessible.

### Minor Observations

| Issue | Device | Severity | Description |
|-------|--------|----------|-------------|
| 1 | iPhone Portrait | Cosmetic | The streak alert dialog has significant empty space between the Outcome Breakdown table and the action buttons at the bottom. This is not a functional issue but could be tightened for a more polished appearance. |
| 2 | All Devices | Cosmetic | When the app first loads with no historical data, the sit-out suggestion defaults to 24 spins. This is a reasonable default, but the dialog text could clarify that this is a default rather than a calculated average. |
| 3 | iPad Landscape | Cosmetic | The splash screen image is smaller relative to the viewport compared to iPhone, leaving more black space around it. Consider scaling the splash image for larger viewports. |

### Previously Reported (User-Identified)

| Issue | Status | Description |
|-------|--------|-------------|
| Pop-ups too large on iPad landscape | To Verify | James noted that some pop-ups may be too big in iPad landscape mode. From screenshot review, all modals appear to fit within the viewport. This may need real-device testing to confirm. |

## Recommendation

The application is in good shape for real-device testing. The minor cosmetic items above are low priority and can be addressed in a future polish pass.
