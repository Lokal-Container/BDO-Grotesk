## Fontbakery report

Fontbakery version: 0.8.11

<details><summary><b>[10] Family checks</b></summary><div><details><summary>🍞 <b>PASS:</b> Checking all files are in the same directory. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/single_directory">com.google.fonts/check/family/single_directory</a>)</summary><div>

>
>If the set of font files passed in the command line is not all in the same directory, then we warn the user since the tool will interpret the set of files as belonging to a single family (and it is unlikely that the user would store the files from a single family spreaded in several separate directories).
>
* 🍞 **PASS** All files are in the same directory.
</div></details><details><summary>🍞 <b>PASS:</b> Each font in a family must have the same set of vertical metrics values. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/vertical_metrics">com.google.fonts/check/family/vertical_metrics</a>)</summary><div>

>
>We want all fonts within a family to have the same vertical metrics so their line spacing is consistent across the family.
>
* 🍞 **PASS** Vertical metrics are the same across the family.
</div></details><details><summary>🍞 <b>PASS:</b> Fonts have equal unicode encodings? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/cmap.html#com.google.fonts/check/family/equal_unicode_encodings">com.google.fonts/check/family/equal_unicode_encodings</a>)</summary><div>


* 🍞 **PASS** Fonts have equal unicode encodings.
</div></details><details><summary>🍞 <b>PASS:</b> Make sure all font files have the same version value. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/head.html#com.google.fonts/check/family/equal_font_versions">com.google.fonts/check/family/equal_font_versions</a>)</summary><div>


* 🍞 **PASS** All font files have the same version.
</div></details><details><summary>🍞 <b>PASS:</b> Fonts have consistent PANOSE proportion? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/family/panose_proportion">com.google.fonts/check/family/panose_proportion</a>)</summary><div>


* 🍞 **PASS** Fonts have consistent PANOSE proportion.
</div></details><details><summary>🍞 <b>PASS:</b> Fonts have consistent PANOSE family type? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/family/panose_familytype">com.google.fonts/check/family/panose_familytype</a>)</summary><div>


* 🍞 **PASS** Fonts have consistent PANOSE family type.
</div></details><details><summary>🍞 <b>PASS:</b> Fonts have consistent underline thickness? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/post.html#com.google.fonts/check/family/underline_thickness">com.google.fonts/check/family/underline_thickness</a>)</summary><div>

>
>Dave C Lemon (Adobe Type Team) recommends setting the underline thickness to be consistent across the family.
>
>If thicknesses are not family consistent, words set on the same line which have different styles look strange.
>
* 🍞 **PASS** Fonts have consistent underline thickness.
</div></details><details><summary>🍞 <b>PASS:</b> Verify that each group of fonts with the same nameID 1 has maximum of 4 fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.adobe.fonts/check/family/max_4_fonts_per_family_name">com.adobe.fonts/check/family/max_4_fonts_per_family_name</a>)</summary><div>

>
>Per the OpenType spec:
>
>'The Font Family name [...] should be shared among at most four fonts that differ only in weight or style [...]'
>
* 🍞 **PASS** There were no more than 4 fonts per family name.
</div></details><details><summary>🍞 <b>PASS:</b> Ensure VFs have 'ital' STAT axis. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/stat.html#com.google.fonts/check/italic_axis_in_stat">com.google.fonts/check/italic_axis_in_stat</a>)</summary><div>

>
>Check that related Upright and Italic VFs have a 'ital' axis in STAT table.
>
* 🍞 **PASS** OK
</div></details><details><summary>💤 <b>SKIP:</b> Check that OS/2.fsSelection bold & italic settings are unique for each NameID1 (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.adobe.fonts/check/family/bold_italic_unique_for_nameid1">com.adobe.fonts/check/family/bold_italic_unique_for_nameid1</a>)</summary><div>

>
>Per the OpenType spec: name ID 1 'is used in combination with Font Subfamily name (name ID 2), and should be shared among at most four fonts that differ only in weight or style.
>
>This four-way distinction should also be reflected in the OS/2.fsSelection field, using bits 0 and 5.
>
* 💤 **SKIP** Unfulfilled Conditions: RIBBI_ttFonts
</div></details><br></div></details><details><summary><b>[95] BDOGrotesk-DemiBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Ensure component transforms do not perform scaling or rotation. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/transformed_components">com.google.fonts/check/transformed_components</a>)</summary><div>

>
>Some families have glyphs which have been constructed by using transformed components e.g the 'u' being constructed from a flipped 'n'.
>
>From a designers point of view, this sounds like a win (less work). However, such approaches can lead to rasterization issues, such as having the 'u' not sitting on the baseline at certain sizes after running the font through ttfautohint.
>
>Other issues are outlines that end up reversed when only one dimension is flipped while the other isn't.
>
>As of July 2019, Marc Foley observed that ttfautohint assigns cvt values to transformed glyphs as if they are not transformed and the result is they render very badly, and that vttLib does not support flipped components.
>
>When building the font with fontmake, the problem can be fixed by adding this to the command line:
>
>--filter DecomposeTransformedComponentsFilter
>
* 🔥 **FAIL** The following glyphs had components with scaling or rotation
or inverted outline direction:

* exclamdown (component exclam)
* backslash (component slash)
* backslash.ss02 (component slash.ss02)
* braceright (component braceleft)
* uni2E29 (component uni2E28)
* braceright.case (component braceleft.case)
* uni3011.case (component uni3010.case)
* uni27E9 (component uni27E8)
* uni27EB (component uni27EA)
* uni27ED (component uni27EC)
* arrowdown (component arrowup)
* arrowleft (component arrowright)
* uni21AA (component uni21A9)
* uni21B3 (component uni21B2)
* uni21BB (component uni21BA)
* uni21CA (component uni21C8)
* arrowdown.ss04 (component arrowup.ss04)
* uni25A8 (component uni25A7)
* uni232B (component uni2326)
* less_hyphen_hyphen.dlig (component arrowright)
 [code: transformed-components]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>

>
>An accent placed on characters with a "soft dot", like i or j, causes the dot to disappear. An explicit dot above can be added where required. See "Diacritics on i and j" in Section 7.1, "Latin" in The Unicode Standard.
>
>Characters with the Soft_Dotted property are listed in https://www.unicode.org/Public/UCD/latest/ucd/PropList.txt
>
* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į̂ į̄ į̌

The dot of soft dotted characters should disappear in other cases, for example: ĭ̦ i̦̇ i̦̊ i̦̋ i̦̒ j̦̀ j̦̄ j̦̆ j̦̇ j̦̈ j̦̊ j̦̋ ǰ̦ j̦̒ į̆ į̇ į̈ į̊ į̋ į̒ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Glyph names are all valid? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/valid_glyphnames">com.google.fonts/check/valid_glyphnames</a>)</summary><div>

>
>Microsoft's recommendations for OpenType Fonts states the following:
>
>'NOTE: The PostScript glyph name must be no longer than 31 characters, include only uppercase or lowercase English letters, European digits, the period or the underscore, i.e. from the set [A-Za-z0-9_.] and should start with a letter, except the special glyph name ".notdef" which starts with a period.'
>
>https://docs.microsoft.com/en-us/typography/opentype/spec/recom#post-table
>
>In practice, though, particularly in modern environments, glyph names can be as long as 63 characters.
>
>According to the "Adobe Glyph List Specification" available at:
>
>https://github.com/adobe-type-tools/agl-specification
>
* ⚠ **WARN** The following glyph names may be too long for some legacy systems which may expect a maximum 31-char length limit:
parenleft_hyphen_greater_parenright.dlig, parenleft_hyphen_greater_greater_parenright.dlig, parenleft_less_hyphen_parenright.dlig and parenleft_less_less_hyphen_parenright.dlig [code: legacy-long-names]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>

>
>Glyphs are either accessible directly through Unicode codepoints or through substitution rules.
>
>In Color Fonts, glyphs are also referenced by the COLR table.
>
>Any glyphs not accessible by either of these means are redundant and serve only to increase the font's file size.
>
* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- Q.SS01

	- aacute.BRACKET.varAlt01

	- abreve.BRACKET.varAlt01

	- acircumflex.BRACKET.varAlt01

	- adieresis.BRACKET.varAlt01

	- agrave.BRACKET.varAlt01

	- amacron.BRACKET.varAlt01

	- aogonek.BRACKET.varAlt01

	- aring.BRACKET.varAlt01

	- arrowdown.ss04 

	- 4 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>

>
>Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be constructured in a handful of ways. This means a glyph's contour count will only differ slightly amongst different fonts, e.g a 'g' could either be 2 or 3 contours, depending on whether its double story or single story.
>
>However, a quotedbl should have 2 contours, unless the font belongs to a display family.
>
>This check currently does not cover variable fonts because there's plenty of alternative ways of constructing glyphs with multiple outlines for each feature in a VarFont. The expected contour count data for this check is currently optimized for the typical construction of glyphs in static fonts.
>
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: oe	Contours detected: 4	Expected: 3

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni21B9	Contours detected: 2	Expected: 4 

	- 18 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>

>
>The dotted circle character (U+25CC) is inserted by shaping engines before mark glyphs which do not have an associated base, especially in the context of broken syllabic clusters.
>
>For fonts containing combining marks, it is recommended that the dotted circle character be included so that these isolated marks can be displayed properly; for fonts supporting complex scripts, this should be considered mandatory.
>
>Additionally, when a dotted circle glyph is present, it should be able to display all marks correctly, meaning that it should contain anchors for all attaching marks.
>
* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>

>
>It is a common practice to have math signs sharing the same width (preferably the same width as tabular figures accross the entire font family).
>
>This probably comes from the will to avoid additional tabular math signs knowing that their design can easily share the same width.
>
* ⚠ **WARN** The most common width is 605 among a set of 4 math glyphs.
The following math glyphs have a different width, though:

Width = 601:
plus

Width = 613:
plusminus, equal

Width = 604:
greater

Width = 603:
logicalnot

Width = 619:
multiply

Width = 602:
minus

Width = 623:
approxequal

Width = 610:
notequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>

>
>This check heuristically looks for on-curve points which are close to, but do not sit on, significant boundary coordinates. For example, a point which has a Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the baseline, here we also check for points near the x-height (but only for lowercase Latin letters), cap-height, ascender and descender Y coordinates.
>
>Not all such misaligned curve points are a mistake, and sometimes the design may call for points in locations near the boundaries. As this check is liable to generate significant numbers of false positives, it will pass if there are more than 100 reported misalignments.
>
* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* parenleft (U+0028): X=126.0,Y=-2.0 (should be at baseline 0?)

	* parenright (U+0029): X=197.5,Y=-2.0 (should be at baseline 0?)

	* f (U+0066): X=96.0,Y=569.0 (should be at x-height 571?)

	* f (U+0066): X=231.0,Y=569.0 (should be at x-height 571?)

	* j (U+006A): X=33.0,Y=-1.0 (should be at baseline 0?)

	* r (U+0072): X=380.0,Y=572.0 (should be at x-height 571?)

	* t (U+0074): X=97.0,Y=569.0 (should be at x-height 571?)

	* t (U+0074): X=233.0,Y=569.0 (should be at x-height 571?)

	* onequarter (U+00BC): X=42.0,Y=-1.0 (should be at baseline 0?)

	* onequarter (U+00BC): X=136.0,Y=-1.0 (should be at baseline 0?) 

	* 90 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>

>
>This check looks for outline segments which seem particularly short (less than 0.6% of the overall path length).
>
>This check is not run for variable fonts, as they may legitimately have short segments. As this check is liable to generate significant numbers of false positives, it will pass if there are more than 100 reported short segments.
>
* ⚠ **WARN** The following glyphs have segments which seem very short:

	* dollar (U+0024) contains a short segment B<<358.0,433.0>-<364.0,432.0>-<370.5,430.5>>

	* dollar (U+0024) contains a short segment B<<370.5,430.5>-<377.0,429.0>-<383.0,428.0>>

	* less (U+003C) contains a short segment L<<197.0,346.0>--<197.0,338.0>>

	* greater (U+003E) contains a short segment L<<407.0,338.0>--<407.0,346.0>>

	* a (U+0061) contains a short segment B<<572.0,98.0>-<584.0,98.0>-<588.0,101.0>>

	* f (U+0066) contains a short segment L<<339.0,683.0>--<333.0,683.0>>

	* r (U+0072) contains a short segment L<<380.0,443.0>--<374.0,443.0>>

	* y (U+0079) contains a short segment L<<72.0,-57.0>--<80.0,-57.0>>

	* ordfeminine (U+00AA) contains a short segment B<<439.0,382.0>-<443.0,382.0>-<446.5,382.5>>

	* ordfeminine (U+00AA) contains a short segment B<<446.5,382.5>-<450.0,383.0>-<454.0,383.0>> 

	* 80 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>

>
>This check looks for consecutive line segments which have the same angle. This normally happens if an outline point has been added by accident.
>
>This check is not run for variable fonts, as they may legitimately have colinear vectors.
>
* ⚠ **WARN** The following glyphs have colinear vectors:

	* exclam (U+0021): L<<115.0,229.0>--<89.0,564.0>> -> L<<89.0,564.0>--<89.0,729.0>>

	* exclam (U+0021): L<<227.0,729.0>--<227.0,564.0>> -> L<<227.0,564.0>--<201.0,229.0>>

	* exclamdown (U+00A1): L<<115.0,342.0>--<89.0,7.0>> -> L<<89.0,7.0>--<89.0,-158.0>>

	* exclamdown (U+00A1): L<<227.0,-158.0>--<227.0,7.0>> -> L<<227.0,7.0>--<201.0,342.0>>

	* radical (U+221A): L<<304.0,407.0>--<304.0,407.0>> -> L<<304.0,407.0>--<305.0,407.0>>

	* uni21BA (U+21BA): L<<498.0,559.0>--<501.0,522.0>> -> L<<501.0,522.0>--<501.0,386.0>>

	* uni21BA (U+21BA): L<<751.0,627.0>--<605.0,627.0>> -> L<<605.0,627.0>--<580.0,628.0>>

	* uni21BB (U+21BB): L<<342.0,559.0>--<339.0,522.0>> -> L<<339.0,522.0>--<339.0,386.0>> 

	* uni21BB (U+21BB): L<<89.0,627.0>--<235.0,627.0>> -> L<<235.0,627.0>--<260.0,628.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>

>
>This check detects line segments which are nearly, but not quite, exactly horizontal or vertical. Sometimes such lines are created by design, but often they are indicative of a design error.
>
>This check is disabled for italic styles, which often contain nearly-upright lines.
>
* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* M (U+004D): L<<726.0,0.0>--<729.0,599.0>>

	* arrowleft (U+2190): L<<254.0,291.0>--<830.0,292.0>>

	* arrowright (U+2192): L<<654.0,291.0>--<78.0,292.0>>

	* five (U+0035): L<<182.0,304.0>--<51.0,303.0>>

	* plus (U+002B): L<<237.0,396.0>--<238.0,608.0>>

	* plus (U+002B): L<<238.0,68.0>--<237.0,287.0>>

	* plus (U+002B): L<<362.0,287.0>--<363.0,68.0>>

	* plus (U+002B): L<<363.0,608.0>--<362.0,396.0>>

	* summation (U+2211): L<<554.0,608.0>--<221.0,607.0>>

	* uni03BC (U+03BC): L<<67.0,-167.0>--<68.0,573.0>> 

	* 3 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><details><summary>💤 <b>SKIP:</b> Check correctness of STAT table strings  (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/STAT_strings">com.google.fonts/check/STAT_strings</a>)</summary><div>

>
>On the STAT table, the "Italic" keyword must not be used on AxisValues for variation axes other than 'ital'.
>
* 💤 **SKIP** Unfulfilled Conditions: has_STAT_table
</div></details><details><summary>💤 <b>SKIP:</b> Each font in set of sibling families must have the same set of vertical metrics values. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/superfamily/vertical_metrics">com.google.fonts/check/superfamily/vertical_metrics</a>)</summary><div>

>
>We may want all fonts within a super-family (all sibling families) to have the same vertical metrics so their line spacing is consistent across the super-family.
>
>This is an experimental extended version of com.google.fonts/check/family/vertical_metrics and for now it will only result in WARNs.
>
* 💤 **SKIP** Sibling families were not detected.
</div></details><details><summary>💤 <b>SKIP:</b> Ensure indic fonts have the Indian Rupee Sign glyph.  (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/rupee">com.google.fonts/check/rupee</a>)</summary><div>

>
>Per Bureau of Indian Standards every font supporting one of the official Indian languages needs to include Unicode Character “₹” (U+20B9) Indian Rupee Sign.
>
* 💤 **SKIP** Unfulfilled Conditions: is_indic_font
</div></details><details><summary>💤 <b>SKIP:</b> Does the font contain chws and vchw features? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/cjk_chws_feature">com.google.fonts/check/cjk_chws_feature</a>)</summary><div>

>
>The W3C recommends the addition of chws and vchw features to CJK fonts to enhance the spacing of glyphs in environments which do not fully support JLREQ layout rules.
>
>The chws_tool utility (https://github.com/googlefonts/chws_tool) can be used to add these features automatically.
>
* 💤 **SKIP** Unfulfilled Conditions: is_cjk_font
</div></details><details><summary>💤 <b>SKIP:</b> Ensure that the font can be rasterized by FreeType. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.adobe.fonts/check/freetype_rasterizer">com.adobe.fonts/check/freetype_rasterizer</a>)</summary><div>

>
>Malformed fonts can cause FreeType to crash.
>
* 💤 **SKIP** FreeType is not available; to install it, invoke the 'freetype' extra when installing Font Bakery. [code: freetype-not-installed]
</div></details><details><summary>💤 <b>SKIP:</b> Detect any interpolation issues in the font. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/interpolation_issues">com.google.fonts/check/interpolation_issues</a>)</summary><div>

>
>When creating a variable font, the designer must make sure that corresponding paths have the same start points across masters, as well as that corresponding component shapes are placed in the same order within a glyph across masters. If this is not done, the glyph will not interpolate correctly.
>
>Here we check for the presence of potential interpolation errors using the fontTools.varLib.interpolatable module.
>
* 💤 **SKIP** Unfulfilled Conditions: is_variable_font
</div></details><details><summary>💤 <b>SKIP:</b> Is the CFF subr/gsubr call depth > 10? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/cff.html#com.adobe.fonts/check/cff_call_depth">com.adobe.fonts/check/cff_call_depth</a>)</summary><div>

>
>Per "The Type 2 Charstring Format, Technical Note #5177", the "Subr nesting, stack limit" is 10.
>
* 💤 **SKIP** Unfulfilled Conditions: is_cff
</div></details><details><summary>💤 <b>SKIP:</b> Is the CFF2 subr/gsubr call depth > 10? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/cff.html#com.adobe.fonts/check/cff2_call_depth">com.adobe.fonts/check/cff2_call_depth</a>)</summary><div>

>
>Per "The CFF2 CharString Format", the "Subr nesting, stack limit" is 10.
>
* 💤 **SKIP** Unfulfilled Conditions: is_cff2
</div></details><details><summary>💤 <b>SKIP:</b> Does the font use deprecated CFF operators or operations? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/cff.html#com.adobe.fonts/check/cff_deprecated_operators">com.adobe.fonts/check/cff_deprecated_operators</a>)</summary><div>

>
>The 'dotsection' operator and the use of 'endchar' to build accented characters from the Adobe Standard Encoding Character Set ("seac") are deprecated in CFF. Adobe recommends repairing any fonts that use these, especially endchar-as-seac, because a rendering issue was discovered in Microsoft Word with a font that makes use of this operation. The check treats that usage as a FAIL. There are no known ill effects of using dotsection, so that check is a WARN.
>
* 💤 **SKIP** Unfulfilled Conditions: is_cff
</div></details><details><summary>💤 <b>SKIP:</b> Checking head.macStyle value. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/head.html#com.google.fonts/check/mac_style">com.google.fonts/check/mac_style</a>)</summary><div>

>
>The values of the flags on the macStyle entry on the 'head' OpenType table that describe whether a font is bold and/or italic must be coherent with the actual style of the font as inferred by its filename.
>
* 💤 **SKIP** Unfulfilled Conditions: style
</div></details><details><summary>💤 <b>SKIP:</b> Checking OS/2 achVendID against configuration. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.thetypefounders/check/vendor_id">com.thetypefounders/check/vendor_id</a>)</summary><div>

>
>When a font project's Vendor ID is specified explicitely on FontBakery's configuration file, all binaries must have a matching vendor identifier value in the OS/2 table.
>
* 💤 **SKIP** Add the `vendor_id` key to a `fontbakery.yaml` file on your font project directory to enable this check.
You'll also need to use the `--configuration` flag when invoking fontbakery.
</div></details><details><summary>💤 <b>SKIP:</b> Checking OS/2 fsSelection value. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/fsselection">com.google.fonts/check/fsselection</a>)</summary><div>


* 💤 **SKIP** Unfulfilled Conditions: style
</div></details><details><summary>💤 <b>SKIP:</b> Checking post.italicAngle value. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/post.html#com.google.fonts/check/italic_angle">com.google.fonts/check/italic_angle</a>)</summary><div>

>
>The 'post' table italicAngle property should be a reasonable amount, likely not more than 30°. Note that in the OpenType specification, the value is negative for a rightward lean.
>
>https://docs.microsoft.com/en-us/typography/opentype/spec/post
>
* 💤 **SKIP** Unfulfilled Conditions: style
</div></details><details><summary>💤 <b>SKIP:</b> CFF table FontName must match name table ID 6 (PostScript name). (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.adobe.fonts/check/name/postscript_vs_cff">com.adobe.fonts/check/name/postscript_vs_cff</a>)</summary><div>

>
>The PostScript name entries in the font's 'name' table should match the FontName string in the 'CFF ' table.
>
>The 'CFF ' table has a lot of information that is duplicated in other tables. This information should be consistent across tables, because there's no guarantee which table an app will get the data from.
>
* 💤 **SKIP** Unfulfilled Conditions: is_cff
</div></details><details><summary>💤 <b>SKIP:</b> The variable font 'wght' (Weight) axis coordinate must be 400 on the 'Regular' instance. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/regular_wght_coord">com.google.fonts/check/varfont/regular_wght_coord</a>)</summary><div>

>
>According to the Open-Type spec's registered design-variation tag 'wght' available at https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wght
>
>If a variable font has a 'wght' (Weight) axis, then the coordinate of its 'Regular' instance is required to be 400.
>
* 💤 **SKIP** Unfulfilled Conditions: is_variable_font, has_wght_axis
</div></details><details><summary>💤 <b>SKIP:</b> The variable font 'wdth' (Width) axis coordinate must be 100 on the 'Regular' instance. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/regular_wdth_coord">com.google.fonts/check/varfont/regular_wdth_coord</a>)</summary><div>

>
>According to the Open-Type spec's registered design-variation tag 'wdth' available at https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wdth
>
>If a variable font has a 'wdth' (Width) axis, then the coordinate of its 'Regular' instance is required to be 100.
>
* 💤 **SKIP** Unfulfilled Conditions: is_variable_font, has_wdth_axis
</div></details><details><summary>💤 <b>SKIP:</b> The variable font 'slnt' (Slant) axis coordinate must be zero on the 'Regular' instance. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/regular_slnt_coord">com.google.fonts/check/varfont/regular_slnt_coord</a>)</summary><div>

>
>According to the Open-Type spec's registered design-variation tag 'slnt' available at https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_slnt
>
>If a variable font has a 'slnt' (Slant) axis, then the coordinate of its 'Regular' instance is required to be zero.
>
* 💤 **SKIP** Unfulfilled Conditions: is_variable_font, has_slnt_axis
</div></details><details><summary>💤 <b>SKIP:</b> The variable font 'ital' (Italic) axis coordinate must be zero on the 'Regular' instance. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/regular_ital_coord">com.google.fonts/check/varfont/regular_ital_coord</a>)</summary><div>

>
>According to the Open-Type spec's registered design-variation tag 'ital' available at https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_ital
>
>If a variable font has a 'ital' (Italic) axis, then the coordinate of its 'Regular' instance is required to be zero.
>
* 💤 **SKIP** Unfulfilled Conditions: is_variable_font, has_ital_axis
</div></details><details><summary>💤 <b>SKIP:</b> The variable font 'opsz' (Optical Size) axis coordinate should be between 10 and 16 on the 'Regular' instance. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/regular_opsz_coord">com.google.fonts/check/varfont/regular_opsz_coord</a>)</summary><div>

>
>According to the Open-Type spec's registered design-variation tag 'opsz' available at https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_opsz
>
>If a variable font has an 'opsz' (Optical Size) axis, then the coordinate of its 'Regular' instance is recommended to be a value in the range 10 to 16.
>
* 💤 **SKIP** Unfulfilled Conditions: is_variable_font, has_opsz_axis
</div></details><details><summary>💤 <b>SKIP:</b> The variable font 'wght' (Weight) axis coordinate must be 700 on the 'Bold' instance. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/bold_wght_coord">com.google.fonts/check/varfont/bold_wght_coord</a>)</summary><div>

>
>The Open-Type spec's registered design-variation tag 'wght' available at https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wght does not specify a required value for the 'Bold' instance of a variable font.
>
>But Dave Crossland suggested that we should enforce a required value of 700 in this case (NOTE: a distinction is made between "no bold instance present" vs "bold instance is present but its wght coordinate is not == 700").
>
* 💤 **SKIP** Unfulfilled Conditions: is_variable_font, has_wght_axis
</div></details><details><summary>💤 <b>SKIP:</b> The variable font 'wght' (Weight) axis coordinate must be within spec range of 1 to 1000 on all instances. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/wght_valid_range">com.google.fonts/check/varfont/wght_valid_range</a>)</summary><div>

>
>According to the Open-Type spec's registered design-variation tag 'wght' available at https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wght
>
>On the 'wght' (Weight) axis, the valid coordinate range is 1-1000.
>
* 💤 **SKIP** Unfulfilled Conditions: is_variable_font, has_wght_axis
</div></details><details><summary>💤 <b>SKIP:</b> The variable font 'wdth' (Width) axis coordinate must strictly greater than zero. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/wdth_valid_range">com.google.fonts/check/varfont/wdth_valid_range</a>)</summary><div>

>
>According to the Open-Type spec's registered design-variation tag 'wdth' available at https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wdth
>
>On the 'wdth' (Width) axis, the valid numeric range is strictly greater than zero.
>
* 💤 **SKIP** Unfulfilled Conditions: is_variable_font, has_wdth_axis
</div></details><details><summary>💤 <b>SKIP:</b> The variable font 'slnt' (Slant) axis coordinate specifies positive values in its range?  (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/slnt_range">com.google.fonts/check/varfont/slnt_range</a>)</summary><div>

>
>The OpenType spec says at https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxistag_slnt that:
>
>[...] the scale for the Slant axis is interpreted as the angle of slant in counter-clockwise degrees from upright. This means that a typical, right-leaning oblique design will have a negative slant value. This matches the scale used for the italicAngle field in the post table.
>
* 💤 **SKIP** Unfulfilled Conditions: is_variable_font, has_slnt_axis
</div></details><details><summary>💤 <b>SKIP:</b> Validates that the value of axisNameID used by each VariationAxisRecord is greater than 255 and less than 32768. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.adobe.fonts/check/varfont/valid_axis_nameid">com.adobe.fonts/check/varfont/valid_axis_nameid</a>)</summary><div>

>
>According to the 'fvar' documentation in OpenType spec v1.9 https://docs.microsoft.com/en-us/typography/opentype/spec/fvar
>
>The axisNameID field provides a name ID that can be used to obtain strings from the 'name' table that can be used to refer to the axis in application user interfaces. The name ID must be greater than 255 and less than 32768.
>
* 💤 **SKIP** Unfulfilled Conditions: is_variable_font
</div></details><details><summary>💤 <b>SKIP:</b> Validates that the value of subfamilyNameID used by each InstanceRecord is 2, 17, or greater than 255 and less than 32768. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.adobe.fonts/check/varfont/valid_subfamily_nameid">com.adobe.fonts/check/varfont/valid_subfamily_nameid</a>)</summary><div>

>
>According to the 'fvar' documentation in OpenType spec v1.9 https://docs.microsoft.com/en-us/typography/opentype/spec/fvar
>
>The subfamilyNameID field provides a name ID that can be used to obtain strings from the 'name' table that can be treated as equivalent to name ID 17 (typographic subfamily) strings for the given instance. Values of 2 or 17 can be used; otherwise, values must be greater than 255 and less than 32768.
>
* 💤 **SKIP** Unfulfilled Conditions: is_variable_font
</div></details><details><summary>💤 <b>SKIP:</b> Validates that the value of postScriptNameID used by each InstanceRecord is 6, 0xFFFF, or greater than 255 and less than 32768. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.adobe.fonts/check/varfont/valid_postscript_nameid">com.adobe.fonts/check/varfont/valid_postscript_nameid</a>)</summary><div>

>
>According to the 'fvar' documentation in OpenType spec v1.9 https://docs.microsoft.com/en-us/typography/opentype/spec/fvar
>
>The postScriptNameID field provides a name ID that can be used to obtain strings from the 'name' table that can be treated as equivalent to name ID 6 (PostScript name) strings for the given instance. Values of 6 and 0xFFFF can be used; otherwise, values must be greater than 255 and less than 32768.
>
* 💤 **SKIP** Unfulfilled Conditions: is_variable_font
</div></details><details><summary>💤 <b>SKIP:</b> Validates that when an instance record is included for the default instance, its subfamilyNameID value is set to a name ID whose string is equal to the string of either name ID 2 or 17, and its postScriptNameID value is set to a name ID whose string is equal to the string of name ID 6. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.adobe.fonts/check/varfont/valid_default_instance_nameids">com.adobe.fonts/check/varfont/valid_default_instance_nameids</a>)</summary><div>

>
>According to the 'fvar' documentation in OpenType spec v1.9.1 https://docs.microsoft.com/en-us/typography/opentype/spec/fvar
>
>The default instance of a font is that instance for which the coordinate value of each axis is the defaultValue specified in the corresponding variation axis record. An instance record is not required for the default instance, though an instance record can be provided. When enumerating named instances, the default instance should be enumerated even if there is no corresponding instance record. If an instance record is included for the default instance (that is, an instance record has coordinates set to default values), then the nameID value should be set to either 2 or 17 or to a name ID with the same value as name ID 2 or 17. Also, if a postScriptNameID is included in instance records, and the postScriptNameID value should be set to 6 or to a name ID with the same value as name ID 6.
>
* 💤 **SKIP** Unfulfilled Conditions: is_variable_font
</div></details><details><summary>💤 <b>SKIP:</b> Validates that all of the instance records in a given font have the same size. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.adobe.fonts/check/varfont/same_size_instance_records">com.adobe.fonts/check/varfont/same_size_instance_records</a>)</summary><div>

>
>According to the 'fvar' documentation in OpenType spec v1.9 https://docs.microsoft.com/en-us/typography/opentype/spec/fvar
>
>All of the instance records in a given font must be the same size, with all either including or omitting the postScriptNameID field. [...] If the value is 0xFFFF, then the value is ignored, and no PostScript name equivalent is provided for the instance.
>
* 💤 **SKIP** Unfulfilled Conditions: is_variable_font
</div></details><details><summary>💤 <b>SKIP:</b> Validates that all of the instance records in a given font have distinct data. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.adobe.fonts/check/varfont/distinct_instance_records">com.adobe.fonts/check/varfont/distinct_instance_records</a>)</summary><div>

>
>According to the 'fvar' documentation in OpenType spec v1.9 https://docs.microsoft.com/en-us/typography/opentype/spec/fvar
>
>All of the instance records in a font should have distinct coordinates and distinct subfamilyNameID and postScriptName ID values. If two or more records share the same coordinates, the same nameID values or the same postScriptNameID values, then all but the first can be ignored.
>
* 💤 **SKIP** Unfulfilled Conditions: is_variable_font
</div></details><details><summary>💤 <b>SKIP:</b> Validate foundry-defined design-variation axis tag names. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.adobe.fonts/check/varfont/foundry_defined_tag_name">com.adobe.fonts/check/varfont/foundry_defined_tag_name</a>)</summary><div>

>
>According to the Open-Type spec's syntactic requirements for foundry-defined design-variation axis tags available at https://learn.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg
>
>Foundry-defined tags must begin with an uppercase letter and must use only uppercase letters or digits.
>
* 💤 **SKIP** Unfulfilled Conditions: is_variable_font
</div></details><details><summary>💤 <b>SKIP:</b> All fvar axes have a correspondent Axis Record on STAT table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/stat.html#com.google.fonts/check/varfont/stat_axis_record_for_each_axis">com.google.fonts/check/varfont/stat_axis_record_for_each_axis</a>)</summary><div>

>
>According to the OpenType spec, there must be an Axis Record for every axis defined in the fvar table.
>
>https://docs.microsoft.com/en-us/typography/opentype/spec/stat#axis-records
>
* 💤 **SKIP** Unfulfilled Conditions: is_variable_font
</div></details><details><summary>💤 <b>SKIP:</b> STAT table has Axis Value tables? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/stat.html#com.adobe.fonts/check/stat_has_axis_value_tables">com.adobe.fonts/check/stat_has_axis_value_tables</a>)</summary><div>

>
>According to the OpenType spec, in a variable font, it is strongly recommended that axis value tables be included for every element of typographic subfamily names for all of the named instances defined in the 'fvar' table.
>
>Axis value tables are particularly important for variable fonts, but can also be used in non-variable fonts. When used in non-variable fonts, axis value tables for particular values should be implemented consistently across fonts in the family.
>
>If present, Format 4 Axis Value tables are checked to ensure they have more than one AxisValueRecord (a strong recommendation from the OpenType spec).
>
>https://docs.microsoft.com/en-us/typography/opentype/spec/stat#axis-value-tables
>
* 💤 **SKIP** Unfulfilled Conditions: has_STAT_table
</div></details><details><summary>💤 <b>SKIP:</b> Ensure 'ital' STAT axis is boolean value (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/stat.html#com.google.fonts/check/italic_axis_in_stat_is_boolean">com.google.fonts/check/italic_axis_in_stat_is_boolean</a>)</summary><div>

>
>Check that the value of the 'ital' STAT axis is boolean (either 0 or 1), and elided for the Upright and not elided for the Italic, and that the Upright is linked to the Italic.
>
* 💤 **SKIP** Unfulfilled Conditions: style, has_STAT_table
</div></details><details><summary>💤 <b>SKIP:</b> Ensure 'ital' STAT axis is last. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/stat.html#com.google.fonts/check/italic_axis_last">com.google.fonts/check/italic_axis_last</a>)</summary><div>

>
>Check that the 'ital' STAT axis is last in axis order.
>
* 💤 **SKIP** Unfulfilled Conditions: style, has_STAT_table
</div></details><details><summary>💤 <b>SKIP:</b> Check that texts shape as per expectation (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/shaping/regression">com.google.fonts/check/shaping/regression</a>)</summary><div>

>
>Fonts with complex layout rules can benefit from regression tests to ensure that the rules are behaving as designed. This checks runs a shaping test suite and compares expected shaping against actual shaping, reporting any differences.
>
>Shaping test suites should be written by the font engineer and referenced in the fontbakery configuration file. For more information about write shaping test files and how to configure fontbakery to read the shaping test suites, see https://simoncozens.github.io/tdd-for-otl/
>
* 💤 **SKIP** Shaping test directory not defined in configuration file
</div></details><details><summary>💤 <b>SKIP:</b> Check that no forbidden glyphs are found while shaping (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/shaping/forbidden">com.google.fonts/check/shaping/forbidden</a>)</summary><div>

>
>Fonts with complex layout rules can benefit from regression tests to ensure that the rules are behaving as designed. This checks runs a shaping test suite and reports if any glyphs are generated in the shaping which should not be produced. (For example, .notdef glyphs, visible viramas, etc.)
>
>Shaping test suites should be written by the font engineer and referenced in the Font Bakery configuration file. For more information about write shaping test files and how to configure fontbakery to read the shaping test suites, see https://simoncozens.github.io/tdd-for-otl/
>
* 💤 **SKIP** Shaping test directory not defined in configuration file
</div></details><details><summary>💤 <b>SKIP:</b> Check that no collisions are found while shaping (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/shaping/collides">com.google.fonts/check/shaping/collides</a>)</summary><div>

>
>Fonts with complex layout rules can benefit from regression tests to ensure that the rules are behaving as designed. This checks runs a shaping test suite and reports instances where the glyphs collide in unexpected ways.
>
>Shaping test suites should be written by the font engineer and referenced in the fontbakery configuration file. For more information about write shaping test files and how to configure fontbakery to read the shaping test suites, see https://simoncozens.github.io/tdd-for-otl/
>
* 💤 **SKIP** Shaping test directory not defined in configuration file
</div></details><details><summary>ℹ <b>INFO:</b> Font contains all required tables? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/required_tables">com.google.fonts/check/required_tables</a>)</summary><div>

>
>According to the OpenType spec https://docs.microsoft.com/en-us/typography/opentype/spec/otff#required-tables
>
>Whether TrueType or CFF outlines are used in an OpenType font, the following tables are required for the font to function correctly:
>
>- cmap (Character to glyph mapping)
>- head (Font header)
>- hhea (Horizontal header)
>- hmtx (Horizontal metrics)
>- maxp (Maximum profile)
>- name (Naming table)
>- OS/2 (OS/2 and Windows specific metrics)
>- post (PostScript information)
>
>The spec also documents that variable fonts require the following table:
>
>- STAT (Style attributes)
>
>Depending on the typeface and coverage of a font, certain tables are recommended for optimum quality.
>
>For example:
>- the performance of a non-linear font is improved if the VDMX, LTSH, and hdmx tables are present.
>- Non-monospaced Latin fonts should have a kern table.
>- A gasp table is necessary if a designer wants to influence the sizes at which grayscaling is used under Windows. Etc.
>
* ℹ **INFO** This font contains the following optional tables:

	- loca

	- GPOS 

	- GSUB [code: optional-tables]
* 🍞 **PASS** Font contains all required tables.
</div></details><details><summary>ℹ <b>INFO:</b> List all superfamily filepaths (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/superfamily/list">com.google.fonts/check/superfamily/list</a>)</summary><div>

>
>This is a merely informative check that lists all sibling families detected by fontbakery.
>
>Only the fontfiles in these directories will be considered in superfamily-level checks.
>
* ℹ **INFO** fonts/ttf [code: family-path]
</div></details><details><summary>🍞 <b>PASS:</b> Name table records must not have trailing spaces. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/name/trailing_spaces">com.google.fonts/check/name/trailing_spaces</a>)</summary><div>


* 🍞 **PASS** No trailing spaces on name table entries.
</div></details><details><summary>🍞 <b>PASS:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and abs(yMin) to accommodate vowel marks.
>
>When the win Metrics are significantly greater than the upm, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 typo values instead. This means the font developer can control the linespacing with the typo values, whilst avoiding clipping by setting the win values to values greater than the yMax and abs(yMin).
>
* 🍞 **PASS** OS/2 usWinAscent & usWinDescent values look good!
</div></details><details><summary>🍞 <b>PASS:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>

>
>OS/2 and hhea vertical metric values should match. This will produce the same linespacing on Mac, GNU+Linux and Windows.
>
>- Mac OS X uses the hhea values.
>- Windows uses OS/2 or Win, depending on the OS or fsSelection bit value.
>
>When OS/2 and hhea vertical metrics match, the same linespacing results on macOS, GNU+Linux and Windows. Unfortunately as of 2018, Google Fonts has released many fonts with vertical metrics that don't match in this way. When we fix this issue in these existing families, we will create a visible change in line/paragraph layout for either Windows or macOS users, which will upset some of them.
>
>But we have a duty to fix broken stuff, and inconsistent paragraph layout is unacceptably broken when it is possible to avoid it.
>
>If users complain and prefer the old broken version, they have the freedom to take care of their own situation.
>
* 🍞 **PASS** OS/2.sTypoAscender/Descender values match hhea.ascent/descent.
</div></details><details><summary>🍞 <b>PASS:</b> Checking with ots-sanitize. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/ots">com.google.fonts/check/ots</a>)</summary><div>


* 🍞 **PASS** ots-sanitize passed this file
</div></details><details><summary>🍞 <b>PASS:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>

>
>Running old versions of FontBakery can lead to a poor report which may include false WARNs and FAILs due do bugs, as well as outdated quality assurance criteria.
>
>Older versions will also not report problems that are detected by new checks added to the tool in more recent updates.
>
* 🍞 **PASS** Font Bakery is up-to-date.
</div></details><details><summary>🍞 <b>PASS:</b> Font contains '.notdef' as its first glyph? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/mandatory_glyphs">com.google.fonts/check/mandatory_glyphs</a>)</summary><div>

>
>The OpenType specification v1.8.2 recommends that the first glyph is the '.notdef' glyph without a codepoint assigned and with a drawing.
>
>https://docs.microsoft.com/en-us/typography/opentype/spec/recom#glyph-0-the-notdef-glyph
>
>Pre-v1.8, it was recommended that fonts should also contain 'space', 'CR' and '.null' glyphs. This might have been relevant for MacOS 9 applications.
>
* 🍞 **PASS** OK
</div></details><details><summary>🍞 <b>PASS:</b> Font contains glyphs for whitespace characters? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphs">com.google.fonts/check/whitespace_glyphs</a>)</summary><div>


* 🍞 **PASS** Font contains glyphs for whitespace characters.
</div></details><details><summary>🍞 <b>PASS:</b> Font has **proper** whitespace glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_glyphnames">com.google.fonts/check/whitespace_glyphnames</a>)</summary><div>

>
>This check enforces adherence to recommended whitespace (codepoints 0020 and 00A0) glyph names according to the Adobe Glyph List.
>
* 🍞 **PASS** Font has **AGL recommended** names for whitespace glyphs.
</div></details><details><summary>🍞 <b>PASS:</b> Whitespace glyphs have ink? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_ink">com.google.fonts/check/whitespace_ink</a>)</summary><div>


* 🍞 **PASS** There is no whitespace glyph with ink.
</div></details><details><summary>🍞 <b>PASS:</b> Are there unwanted tables? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unwanted_tables">com.google.fonts/check/unwanted_tables</a>)</summary><div>

>
>Some font editors store source data in their own SFNT tables, and these can sometimes sneak into final release files, which should only have OpenType spec tables.
>
* 🍞 **PASS** There are no unwanted tables.
</div></details><details><summary>🍞 <b>PASS:</b> Font contains unique glyph names? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unique_glyphnames">com.google.fonts/check/unique_glyphnames</a>)</summary><div>

>
>Duplicate glyph names prevent font installation on Mac OS X.
>
* 🍞 **PASS** Font contains unique glyph names.
</div></details><details><summary>🍞 <b>PASS:</b> Checking with fontTools.ttx (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/ttx_roundtrip">com.google.fonts/check/ttx_roundtrip</a>)</summary><div>


* 🍞 **PASS** Hey! It all looks good!
</div></details><details><summary>🍞 <b>PASS:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>

>
>The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation.
>
>It is supposed to be zero-width and invisible.
>
>It is also mostly an obsolete mechanism now, and the character is typicaly only included in fonts for legacy codepage coverage.
>
* 🍞 **PASS** Looks good!
</div></details><details><summary>🍞 <b>PASS:</b> Ensure no GPOS7 lookups are present. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/gpos7">com.google.fonts/check/gpos7</a>)</summary><div>

>
>Versions of fonttools >=4.14.0 (19 August 2020) perform an optimisation on chained contextual lookups, expressing GSUB6 as GSUB5 and GPOS8 and GPOS7 where possible (when there are no suffixes/prefixes for all rules in the lookup).
>
>However, makeotf has never generated these lookup types and they are rare in practice. Perhaps before of this, Mac's CoreText shaper does not correctly interpret GPOS7, meaning that these lookups will be ignored by the shaper, and fonts containing these lookups will have unintended positioning errors.
>
>To fix this warning, rebuild the font with a recent version of fonttools.
>
* 🍞 **PASS** Font has no GPOS7 lookups
</div></details><details><summary>🍞 <b>PASS:</b> Font has the proper sfntVersion value? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.adobe.fonts/check/sfnt_version">com.adobe.fonts/check/sfnt_version</a>)</summary><div>

>
>OpenType fonts that contain TrueType outlines should use the value of 0x00010000 for the sfntVersion. OpenType fonts containing CFF data (version 1 or 2) should use 0x4F54544F ('OTTO', when re-interpreted as a Tag) for sfntVersion.
>
>Fonts with the wrong sfntVersion value are rejected by FreeType.
>
>https://docs.microsoft.com/en-us/typography/opentype/spec/otff#table-directory
>
* 🍞 **PASS** Font has the correct sfntVersion value.
</div></details><details><summary>🍞 <b>PASS:</b> Space and non-breaking space have the same width? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/whitespace_widths">com.google.fonts/check/whitespace_widths</a>)</summary><div>

>
>If the space and nbspace glyphs have different widths, then Google Workspace has problems with the font.
>
>The nbspace is used to replace the space character in multiple situations in documents; such as the space before punctuation in languages that do that. It avoids the punctuation to be separated from the last word and go to next line.
>
>This is automatic substitution by the text editors, not by fonts. It is also used by designers in text composition practice to create nicely shaped paragraphs. If the space and the nbspace are not the same width, it breaks the text composition of documents.
>
* 🍞 **PASS** Space and non-breaking space have the same width.
</div></details><details><summary>🍞 <b>PASS:</b> Checking unitsPerEm value is reasonable. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/head.html#com.google.fonts/check/unitsperem">com.google.fonts/check/unitsperem</a>)</summary><div>

>
>According to the OpenType spec:
>
>The value of unitsPerEm at the head table must be a value between 16 and 16384. Any value in this range is valid.
>
>In fonts that have TrueType outlines, a power of 2 is recommended as this allows performance optimizations in some rasterizers.
>
>But 1000 is a commonly used value. And 2000 may become increasingly more common on Variable Fonts.
>
* 🍞 **PASS** The unitsPerEm value (1000) on the 'head' table is reasonable.
</div></details><details><summary>🍞 <b>PASS:</b> Checking font version fields (head and name table). (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/head.html#com.google.fonts/check/font_version">com.google.fonts/check/font_version</a>)</summary><div>


* 🍞 **PASS** All font version fields match.
</div></details><details><summary>🍞 <b>PASS:</b> Check if OS/2 xAvgCharWidth is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/xavgcharwidth">com.google.fonts/check/xavgcharwidth</a>)</summary><div>


* 🍞 **PASS** OS/2 xAvgCharWidth value is correct.
</div></details><details><summary>🍞 <b>PASS:</b> Check if OS/2 fsSelection matches head macStyle bold and italic bits. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.adobe.fonts/check/fsselection_matches_macstyle">com.adobe.fonts/check/fsselection_matches_macstyle</a>)</summary><div>

>
>The bold and italic bits in OS/2.fsSelection must match the bold and italic bits in head.macStyle per the OpenType spec.
>
* 🍞 **PASS** The OS/2.fsSelection and head.macStyle bold and italic settings match.
</div></details><details><summary>🍞 <b>PASS:</b> Check code page character ranges (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/code_pages">com.google.fonts/check/code_pages</a>)</summary><div>

>
>At least some programs (such as Word and Sublime Text) under Windows 7 do not recognize fonts unless code page bits are properly set on the ulCodePageRange1 (and/or ulCodePageRange2) fields of the OS/2 table.
>
>More specifically, the fonts are selectable in the font menu, but whichever Windows API these applications use considers them unsuitable for any character set, so anything set in these fonts is rendered with Arial as a fallback font.
>
>This check currently does not identify which code pages should be set. Auto-detecting coverage is not trivial since the OpenType specification leaves the interpretation of whether a given code page is "functional" or not open to the font developer to decide.
>
>So here we simply detect as a FAIL when a given font has no code page declared at all.
>
* 🍞 **PASS** At least one code page is defined.
</div></details><details><summary>🍞 <b>PASS:</b> Font has correct post table version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/post.html#com.google.fonts/check/post_table_version">com.google.fonts/check/post_table_version</a>)</summary><div>

>
>Format 2.5 of the 'post' table was deprecated in OpenType 1.3 and should not be used.
>
>According to Thomas Phinney, the possible problem with post format 3 is that under the right combination of circumstances, one can generate PDF from a font with a post format 3 table, and not have accurate backing store for any text that has non-default glyphs for a given codepoint.
>
>It will look fine but not be searchable. This can affect Latin text with high-end typography, and some complex script writing systems, especially with higher-quality fonts. Those circumstances generally involve creating a PDF by first printing a PostScript stream to disk, and then creating a PDF from that stream without reference to the original source document. There are some workflows where this applies,but these are not common use cases.
>
>Apple recommends against use of post format version 4 as "no longer necessary and should be avoided". Please see the Apple TrueType reference documentation for additional details.
>
>https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6post.html
>
>Acceptable post format versions are 2 and 3 for TTF and OTF CFF2 builds, and post format 3 for CFF builds.
>
* 🍞 **PASS** Font has an acceptable post format 2.0 table version.
</div></details><details><summary>🍞 <b>PASS:</b> Check name table for empty records. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.adobe.fonts/check/name/empty_records">com.adobe.fonts/check/name/empty_records</a>)</summary><div>

>
>Check the name table for empty records, as this can cause problems in Adobe apps.
>
* 🍞 **PASS** No empty name table records found.
</div></details><details><summary>🍞 <b>PASS:</b> Description strings in the name table must not contain copyright info. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/name/no_copyright_on_description">com.google.fonts/check/name/no_copyright_on_description</a>)</summary><div>


* 🍞 **PASS** Description strings in the name table do not contain any copyright string.
</div></details><details><summary>🍞 <b>PASS:</b> Checking correctness of monospaced metadata. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/monospace">com.google.fonts/check/monospace</a>)</summary><div>

>
>There are various metadata in the OpenType spec to specify if a font is monospaced or not. If the font is not truly monospaced, then no monospaced metadata should be set (as sometimes they mistakenly are...)
>
>Requirements for monospace fonts:
>
>* post.isFixedPitch - "Set to 0 if the font is proportionally spaced, non-zero if the font is not proportionally spaced (monospaced)" (https://www.microsoft.com/typography/otspec/post.htm)
>
>* hhea.advanceWidthMax must be correct, meaning no glyph's width value is greater. (https://www.microsoft.com/typography/otspec/hhea.htm)
>
>* OS/2.panose.bProportion must be set to 9 (monospace) on latin text fonts.
>
>* OS/2.panose.bSpacing must be set to 3 (monospace) on latin hand written or latin symbol fonts.
>
>* Spec says: "The PANOSE definition contains ten digits each of which currently describes up to sixteen variations. Windows uses bFamilyType, bSerifStyle and bProportion in the font mapper to determine family type. It also uses bProportion to determine if the font is monospaced." (https://www.microsoft.com/typography/otspec/os2.htm#pan https://monotypecom-test.monotype.de/services/pan2)
>
>* OS/2.xAvgCharWidth must be set accurately. "OS/2.xAvgCharWidth is used when rendering monospaced fonts, at least by Windows GDI" (http://typedrawers.com/discussion/comment/15397/#Comment_15397)
>
>Also we should report an error for glyphs not of average width.
>
>Please also note:
>
>Thomas Phinney told us that a few years ago (as of December 2019), if you gave a font a monospace flag in Panose, Microsoft Word would ignore the actual advance widths and treat it as monospaced.
>
>Source: https://typedrawers.com/discussion/comment/45140/#Comment_45140
>
* 🍞 **PASS** Font is not monospaced and all related metadata look good. [code: good]
</div></details><details><summary>🍞 <b>PASS:</b> Does full font name begin with the font family name? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/name/match_familyname_fullfont">com.google.fonts/check/name/match_familyname_fullfont</a>)</summary><div>

>
>The FULL_FONT_NAME entry in the ‘name’ table should start with the same string as the Family Name (FONT_FAMILY_NAME, TYPOGRAPHIC_FAMILY_NAME or WWS_FAMILY_NAME).
>
>If the Family Name is not included as the first part of the Full Font Name, and the user embeds the font in a document using a Microsoft Office app, the app will fail to render the font when it opens the document again.
>
>NOTE: Up until version 1.5, the OpenType spec included the following exception in the definition of Full Font Name:
>
>"An exception to the [above] definition of Full font name is for Microsoft platform strings for CFF OpenType fonts: in this case, the Full font name string must be identical to the PostScript FontName in the CFF Name INDEX."
>
>https://docs.microsoft.com/en-us/typography/opentype/otspec150/name#name-ids
>
* 🍞 **PASS** Full font name begins with the font family name.
</div></details><details><summary>🍞 <b>PASS:</b> Font follows the family naming recommendations? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/family_naming_recommendations">com.google.fonts/check/family_naming_recommendations</a>)</summary><div>


* 🍞 **PASS** Font follows the family naming recommendations.
</div></details><details><summary>🍞 <b>PASS:</b> Name table ID 6 (PostScript name) must be consistent across platforms. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.adobe.fonts/check/name/postscript_name_consistency">com.adobe.fonts/check/name/postscript_name_consistency</a>)</summary><div>

>
>The PostScript name entries in the font's 'name' table should be consistent across platforms.
>
>This is the TTF/CFF2 equivalent of the CFF 'name/postscript_vs_cff' check.
>
* 🍞 **PASS** Entries in the "name" table for ID 6 (PostScript name) are consistent.
</div></details><details><summary>🍞 <b>PASS:</b> Does the number of glyphs in the loca table match the maxp table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/loca.html#com.google.fonts/check/loca/maxp_num_glyphs">com.google.fonts/check/loca/maxp_num_glyphs</a>)</summary><div>


* 🍞 **PASS** 'loca' table matches numGlyphs in 'maxp' table.
</div></details><details><summary>🍞 <b>PASS:</b> Checking Vertical Metric Linegaps. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/hhea.html#com.google.fonts/check/linegaps">com.google.fonts/check/linegaps</a>)</summary><div>


* 🍞 **PASS** OS/2 sTypoLineGap and hhea lineGap are both 0.
</div></details><details><summary>🍞 <b>PASS:</b> MaxAdvanceWidth is consistent with values in the Hmtx and Hhea tables? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/hhea.html#com.google.fonts/check/maxadvancewidth">com.google.fonts/check/maxadvancewidth</a>)</summary><div>


* 🍞 **PASS** MaxAdvanceWidth is consistent with values in the Hmtx and Hhea tables.
</div></details><details><summary>🍞 <b>PASS:</b> Check hhea.caretSlopeRise and hhea.caretSlopeRun (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/hhea.html#com.google.fonts/check/caret_slope">com.google.fonts/check/caret_slope</a>)</summary><div>

>
>Checks whether hhea.caretSlopeRise and hhea.caretSlopeRun match with post.italicAngle.
>
>For Upright fonts, you can set hhea.caretSlopeRise to 1 and hhea.caretSlopeRun to 0.
>
>For Italic fonts, you can set hhea.caretSlopeRise to head.unitsPerEm and calculate hhea.caretSlopeRun like this: round(math.tan(math.radians(-1 * font["post"].italicAngle)) * font["head"].unitsPerEm)
>
>This check allows for a 0.1° rounding difference between the Italic angle as calculated by the caret slope and post.italicAngle
>
* 🍞 **PASS** hhea.caretSlopeRise and hhea.caretSlopeRun match with post.italicAngle.
</div></details><details><summary>🍞 <b>PASS:</b> Does the font have a DSIG table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/dsig.html#com.google.fonts/check/dsig">com.google.fonts/check/dsig</a>)</summary><div>

>
>Microsoft Office 2013 and below products expect fonts to have a digital signature declared in a DSIG table in order to implement OpenType features. The EOL date for Microsoft Office 2013 products is 4/11/2023. This issue does not impact Microsoft Office 2016 and above products.
>
>As we approach the EOL date, it is now considered better to completely remove the table.
>
>But if you still want your font to support OpenType features on Office 2013, then you may find it handy to add a fake signature on a placeholder DSIG table by running one of the helper scripts provided at https://github.com/googlefonts/gftools
>
>Reference: https://github.com/googlefonts/fontbakery/issues/1845
>
* 🍞 **PASS** ok
</div></details><details><summary>🍞 <b>PASS:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>

>
>Glyphs in the GDEF mark glyph class should be non-spacing.
>
>Spacing glyphs in the GDEF mark glyph class may have incorrect anchor positioning that was only intended for building composite glyphs during design.
>
* 🍞 **PASS** Font does not has spacing glyphs in the GDEF mark glyph class.
</div></details><details><summary>🍞 <b>PASS:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>

>
>Mark characters should be in the GDEF mark glyph class.
>
* 🍞 **PASS** Font does not have mark characters not in the GDEF mark glyph class.
</div></details><details><summary>🍞 <b>PASS:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>

>
>Glyphs in the GDEF mark glyph class become non-spacing and may be repositioned if they have mark anchors.
>
>Only combining mark glyphs should be in that class. Any non-mark glyph must not be in that class, in particular spacing glyphs.
>
* 🍞 **PASS** Font does not have non-mark characters in the GDEF mark glyph class.
</div></details><details><summary>🍞 <b>PASS:</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gpos.html#com.google.fonts/check/gpos_kerning_info">com.google.fonts/check/gpos_kerning_info</a>)</summary><div>


* 🍞 **PASS** GPOS table check for kerning information passed.
</div></details><details><summary>🍞 <b>PASS:</b> Is there a usable "kern" table declared in the font? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/kern.html#com.google.fonts/check/kern_table">com.google.fonts/check/kern_table</a>)</summary><div>

>
>Even though all fonts should have their kerning implemented in the GPOS table, there may be kerning info at the kern table as well.
>
>Some applications such as MS PowerPoint require kerning info on the kern table. More specifically, they require a format 0 kern subtable from a kern table version 0 with only glyphs defined in the cmap table, which is the only one that Windows understands (and which is also the simplest and more limited of all the kern subtables).
>
>Google Fonts ingests fonts made for download and use on desktops, and does all web font optimizations in the serving pipeline (using libre libraries that anyone can replicate.)
>
>Ideally, TTFs intended for desktop users (and thus the ones intended for Google Fonts) should have both KERN and GPOS tables.
>
>Given all of the above, we currently treat kerning on a v0 kern table as a good-to-have (but optional) feature.
>
* 🍞 **PASS** Font does not declare an optional "kern" table.
</div></details><details><summary>🍞 <b>PASS:</b> Is there any unused data at the end of the glyf table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/glyf.html#com.google.fonts/check/glyf_unused_data">com.google.fonts/check/glyf_unused_data</a>)</summary><div>


* 🍞 **PASS** There is no unused data at the end of the glyf table.
</div></details><details><summary>🍞 <b>PASS:</b> Check for points out of bounds. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/glyf.html#com.google.fonts/check/points_out_of_bounds">com.google.fonts/check/points_out_of_bounds</a>)</summary><div>


* 🍞 **PASS** All glyph paths have coordinates within bounds!
</div></details><details><summary>🍞 <b>PASS:</b> Check glyphs do not have duplicate components which have the same x,y coordinates. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/glyf.html#com.google.fonts/check/glyf_non_transformed_duplicate_components">com.google.fonts/check/glyf_non_transformed_duplicate_components</a>)</summary><div>

>
>There have been cases in which fonts had faulty double quote marks, with each of them containing two single quote marks as components with the same x, y coordinates which makes them visually look like single quote marks.
>
>This check ensures that glyphs do not contain duplicate components which have the same x,y coordinates.
>
* 🍞 **PASS** Glyphs do not contain duplicate components which have the same x,y coordinates.
</div></details><details><summary>🍞 <b>PASS:</b> Does the font have any invalid feature tags? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/layout.html#com.google.fonts/check/layout_valid_feature_tags">com.google.fonts/check/layout_valid_feature_tags</a>)</summary><div>

>
>Incorrect tags can be indications of typos, leftover debugging code or questionable approaches, or user error in the font editor. Such typos can cause features and language support to fail to work as intended.
>
* 🍞 **PASS** No invalid feature tags were found
</div></details><details><summary>🍞 <b>PASS:</b> Does the font have any invalid script tags? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/layout.html#com.google.fonts/check/layout_valid_script_tags">com.google.fonts/check/layout_valid_script_tags</a>)</summary><div>

>
>Incorrect script tags can be indications of typos, leftover debugging code or questionable approaches, or user error in the font editor. Such typos can cause features and language support to fail to work as intended.
>
* 🍞 **PASS** No invalid script tags were found
</div></details><details><summary>🍞 <b>PASS:</b> Does the font have any invalid language tags? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/layout.html#com.google.fonts/check/layout_valid_language_tags">com.google.fonts/check/layout_valid_language_tags</a>)</summary><div>

>
>Incorrect language tags can be indications of typos, leftover debugging code or questionable approaches, or user error in the font editor. Such typos can cause features and language support to fail to work as intended.
>
* 🍞 **PASS** No invalid language tags were found
</div></details><details><summary>🍞 <b>PASS:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>

>
>This check heuristically detects outline segments which form a particularly small angle, indicative of an outline error. This may cause false positives in cases such as extreme ink traps, so should be regarded as advisory and backed up by manual inspection.
>
* 🍞 **PASS** No jaggy segments found.
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 2 | 9 | 38 | 2 | 54 | 0 |
| 0% | 2% | 9% | 36% | 2% | 51% | 0% |
