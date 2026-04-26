# Subtitle Guidelines {#Subtitle-Guidelines}

<style>
.example {
  font-family: monospace;
  background-color: #f5f5f5;
  padding: 2px 6px;
  border: 1px solid #ddd;
  border-radius: 3px;
}
.flag-online {
  background-color: #e6f3ff;
  color: #0066cc;
  padding: 1px 4px;
  border-radius: 2px;
  font-size: 0.9em;
  text-decoration: none;
}
.flag-broadcast {
  background-color: #fff3e6;
  color: #cc6600;
  padding: 1px 4px;
  border-radius: 2px;
  font-size: 0.9em;
  text-decoration: none;
}
.diagram-annotation {
  font-style: italic;
  color: #666;
}
.diagram-icon.icon-good::before { content: "✓ "; color: green; }
.diagram-icon.icon-bad::before { content: "✗ "; color: red; }
</style>

Version 1.2.5 | March 2026

## OVERVIEW {#OVERVIEW}

### 1 Introduction {#Introduction}
- The BBC Academy has produced an [online guide to subtitling](https://www.bbc.co.uk/guides/zmgnng8). If you are new to subtitling, please start there.

Subtitles are primarily intended to serve viewers with loss of hearing, but they are used by a wide range of people: [around 10% of broadcast viewers use subtitles regularly, increasing to 35% for some online content](https://downloads.bbc.co.uk/rd/pubs/whp/whp-pdf-files/WHP323.pdf).
The majority of these viewers are not hard of hearing.

This document describes 'closed' subtitles only, also known as 'closed captions'. Typically delivered as a separate file, closed subtitles can be switched off by the user and are not 'burnt in' to the image.

There are many formats in circulation for subtitle files. Common formats include SRT, VTT, and ASS.

The Subtitle Guidelines describe best practice for authoring subtitles and provide instructions for making subtitle files for the BBC. This document brings together [documents previously published by Ofcom and the BBC](#Appendix-References) and is intended to serve as the basis for all subtitle work across the BBC: prepared and live, online and broadcast, internal and supplied.

**Who should read this?**

Anyone providing or handling subtitles for the BBC:
- authors of subtitle (respeakers, stenographers, editors);
- producers and distributors of content;
- developers of software tools for authoring, validating, converting and presenting subtitles;
- anyone involved in controlling subtitle quality and compliance.

In addition, if you have an interest in accessibility you will find a lot of useful information here.

**What prior knowledge is expected?**

The editorial guidelines in the [Presentation section](#presentation) are written in plain English, requiring only general familiarity with subtitles. In contrast, to follow the technical instructions in format-specific documentation you will need good working knowledge of XML and CSS. It is recommended that you familiarise yourself with [SMPTE timecodes](https://dx.doi.org/10.5594/SMPTE.ST12-1.2014).

**What should I read for...**
- **An overview of subtitles:** read this introduction and the first few sections of [Presentation](#presentation), [Timing](#Timing), [Identifying speakers](#Identifying-speakers). Scanning through the <samp class="example">examples</samp> will also give you a good understanding of how subtitles are made.
- **Editing and styling subtitles:** read the [Presentation](#presentation) section for text, format and timing guidelines.
- **Making subtitle files:** refer to format-specific documentation for SRT, VTT, or ASS.
**Further assistance**

Assistance with these guidelines and specific technical questions can be emailed to [subtitle-guidelines@bbc.co.uk](mailto:subtitle-guidelines@bbc.co.uk). For help with requirements for specific subtitle documents contact the commissioning
editor.

#### 1.1 Document conventions {#Document-conventions}

The following symbols are used throughout this document.

<samp class="example">Examples</samp> indicate the appearance of a subtitle. When illustrating bad or unrecommended practice, the example has a strike-though, like this: <samp class="example"><s>counter-example</s></samp>. Note that the subtitle style used here is only an approximation. It should not be used as a reference for real-world files or processors.

Most of this document applies to both online and broadcast subtitles. When there are differences between subtitles intended for either platform, this is indicated with one of these flags:

<u class="flag-online">online</u> - applies only to subtitles for online use (not for broadcast).

<u class="flag-broadcast">broadcast</u> - applies to broadcast-only subtitles (not online).
 When no broadcast or online flag is indicated, the text applies to all subtitles.

The guidelines below apply broadly to common subtitle formats like SRT, VTT, and ASS.

Specific actual values are indicated with double quotes, like this: `"2"`. These values must be used without the quotes. Descriptions of values are given in brackets: `[a number between 1 and 3]`. When several values
are possible, they are separated by a pipe: `"1" | "2" | "3"`.

<aside aria-description="Developer information">
Text intended to guide developers in how to meet editorial guidelines is placed in sections like this within the Presentation section.
</aside>

Example sections are inset and styled with a side border.

```
<!-- Subtitle format code examples -->
```

#### 1.2 Navigation {#Navigation}

Since this is a longish sort of a document, we've added in some features to help navigation:
- When the window is wide enough, the table of contents appears on the left-hand side instead of the top.
- The table of contents by default just shows the top level headings - headings with a chevron to the right of them, can be expanded by clicking the chevron.
- If you want a direct link to a given section, you can click on the link icon to the right-hand side of the heading.
- Clicking on a heading in the main part of the document will make sure the heading is visible in the table of contents.

#### 1.3 Document status {#Document-status}

This version covers editorial and technical contribution and presentation guidelines, including resources to assist developers in meeting these guidelines. Future versions will build on these guidelines or describe changes, or address issues
raised. We intend to release small updates often.

##### 1.3.1 Changes since September 2016 {#Changes-since-September-2016}

Amongst many smaller tweaks, the following changes accumulated so far since version 1, released in September 2016, are notable:
- Minor clarifications to presentation guidelines in response to comments received, for example:
- the wording about use of reaction shots to gain time.
- the word rate for live subtitles has been adjusted to 160-180wpm from 130-150wpm.
- the use of numbers.
- capitalisation in speech.
- Technical details moved to the end, in the [File Format](#FILE-FORMAT) section, including specification references and BBC-specific requirements.
- Added details about delivery.
- Added links from the presentation sections to the technical implementation details.
- Added links from the technical implementation details to the presentation requirements they support.
- Added anchor links by headings for ease of reference.
- Made table of contents expandable, set to include top level details only on load.
- Accessibility improvements.
- Added details on positioning.
- Added more details about authoring and presentation font family, font size and line height, size customisation options and the use of Reith Sans font.
- Updated the references.
- Improved formatting of examples, code blocks and requirements.
- Made page layout more responsive to work better with smaller and larger screens.
- Improved accessibility and table of contents.
- Removed the outdated requirement to adjust the font size and line height when using the Reith Sans font.
- Updated workflow diagram in [Appendix - BBC subtitle workflows](#Appendix-BBC-subtitle-workflows) to reflect improvements made over time.
- Added size and position guidance for 9:16 aspect ratio (vertical) video as distinct from 16:9, 4:3 or 1:1 aspect ratio video.
- Restricted duration of [subtitle zero](#Subtitle-zero) to a maximum of 3 frames.
- Improved size and position guidance and font size and line height guidance for each aspect ratio of video.

Thank you to everyone who has helped to review this version. You know who you are!

#### 1.4 How to contribute {#How-to-contribute}

Queries and comments may be raised at any time on the [subtitle guidelines github project](https://github.com/bbc/subtitle-guidelines) by those with
*sufficient project access levels*. Readers who do not have access to the project should email
[subtitle-guidelines@bbc.co.uk](mailto:subtitle-guidelines@bbc.co.uk).

When raising new issues please summarise in a short line the issue in the Title field and include enough information in the Description field, as well as the selected text, to allow the team to identify the relevant part(s) of the document.

## PRESENTATION {#PRESENTATION}

Good subtitling is an art that requires negotiating conflicting requirements. On the whole, you should aim for subtitles that are faithful to the audio. However, you will need to balance this against considerations such as the action on the
screen, speed of speech or editing and visual content.

For example, if you subtitle a scene where a character is speaking rapidly, these are some of the decisions you may have to make:
- Can viewers read the subtitles at the rate of speech?
- Should you edit out some words to allow more time?
- Can subtitles carry over to the next scene so they ‘catch up’ with the speaker?
- Should you use cumulative subtitles to convey the rhythm of speech (for example, if rapping)?
- If there are shot changes within the sequence, should the subtitles be synchronised with those?
- Should you use one, two or three lines of subtitles?
- Should you change the position of the subtitle to avoid obscuring important visual information or to indicate the speaker?

Clearly, it is not possible (or advisable) to provide a set of hard rules that cover all situations. Instead, this document provides some guidelines and practical advice. Their implementation will depend on the content, the genre and on the
subtitler’s expertise.

### 2 Editing text {#Editing-text}

#### 2.1 Prefer verbatim {#Prefer-verbatim}

If there is time for verbatim speech, do not edit unnecessarily. Your aim should be to give the viewer as much access to the soundtrack as you possibly can within the constraints of time, space, shot changes, and on-screen visuals, etc. You
should never deprive the viewer of words/sounds when there is time to include them and where there is no conflict with the visual information.

However, if you have a very "busy" scene, full of action and disconnected conversations, it might be confusing if you subtitle fragments of speech here and there, rather than allowing the viewer to watch what is going on.

Don't automatically edit out words like "but", "so" or "too". They may be short but they are often essential for expressing meaning.

Similarly, conversational phrases like "you know", "well", "actually" often add flavour to the text.

#### 2.2 Don’t simplify {#Don-t-simplify}

It is not necessary to simplify or translate for deaf or hard-of-hearing viewers. This is not only condescending, it is also frustrating for lip-readers.

#### 2.3 Retain speaker’s first and last words {#Retain-speaker-s-first-and-last-words}

If the speaker is in shot, try to retain the start and end of their speech, as these are most obvious to lip-readers who will feel cheated if these words are removed.

#### 2.4 Edit evenly {#Edit-evenly}

Do not take the easy way out by simply removing an entire sentence. Sometimes this will be appropriate, but normally you should aim to edit out a bit of every sentence.

#### 2.5 Keep names {#Keep-names}

Avoid editing out names when they are used to address people. They are often easy targets, but can be essential for following the plot.

#### 2.6 Preserve the style {#Preserve-the-style}

Your editing should be faithful to the speaker's style of speech, taking into account register, nationality, era, etc. This will affect your choice of vocabulary. For instance:
- register: mother vs mum; deceased vs dead; intercourse vs sex;
- nationality: mom vs mum; trousers vs pants;
- era: wireless vs radio; hackney cab vs taxi.

Similarly, make sure if you edit by using contractions that they are appropriate to the context and register. In a formal context, where a speaker would not use contractions, you should not use them either.

Regional styles must also be considered: e.g. it will not always be appropriate to edit "I've got a cat" to "I've a cat"; and "I used to go there" cannot necessarily be edited to "I'd go there."

#### 2.7 Consider the previous subtitle {#Consider-the-previous-subtitle}

Having edited one subtitle, bear your edit in mind when creating the next subtitle. The edit can affect the content as well as the structure of anything that follows.

#### 2.8 Keep the form of the verb {#Keep-the-form-of-the-verb}

Avoid editing by changing the form of a verb. This sometimes works, but more often than not the change of tense produces a nonsense sentence. Also, if you do edit the tense, you have to make it consistent throughout the rest of the text.

#### 2.9 Keep words that can be easily lip-read {#Keep-words-that-can-be-easily-lip-read}

Sometimes speakers can be clearly lip-read - particularly in close-ups. Do not edit out words that can be clearly lip-read. This makes the viewer feel cheated. If editing is unavoidable, then try to edit by using words that have similar lip-movements.
Also, keep as close as possible to the original word order.

#### 2.10 Subtitle illegible text {#Subtitle-illegible-text}

If the onscreen graphics are not easily legible because of the streamed image size or quality, the subtitles must include any text contained within those graphics which provide contextual information. This must include the speaker’s identity,
what they do and any organisations they represent. Other displayed information affected by legibility problems that must be included in the subtitle includes; phone numbers, email addresses, postal addresses, website URLs, or other contact
information.

If the information contained within the graphics is off-topic from what is being spoken, then the information should not be replicated in the subtitle.

#### 2.11 Strong language {#Strong-language}

Do not edit out strong language unless it is absolutely impossible to edit elsewhere in the sentence - deaf or hard-of-hearing viewers find this extremely irritating and condescending.

If the BBC has decided to edit any strong language, then your subtitles must reflect this in the following ways.

##### 2.11.1 Bleeped words {#Bleeped-words}

If the offending word is bleeped, put the word BLEEP in the appropriate place in the subtitle - in caps, in a contrasting colour and without an exclamation mark.

<samp class="example">BLEEP</samp>

If only the middle section of a word is bleeped, do not change colour mid-word:

<samp class="example">f-BLEEP-ing</samp>

##### 2.11.2 Dubbed words {#Dubbed-words}

If the word is dubbed with a euphemistic replacement - e.g. frigging - put this in. If the word is non-standard but spellable put this in, too:

<samp class="example">frerlking</samp>

If the word is dubbed with an unrecognisable sequence of noises, leave them out.

##### 2.11.3 Muted words {#Muted-words}

If the sound is dipped for a portion of the word, put up the sounds that you can hear and three dots for the dipped bit:

<samp class="example">Keep your f...ing
nose out of it!.</samp>

Never use more than three dots.

If the word is mouthed, use a label:

<samp class="example">So (MOUTHS) f...ing
what?</samp>

### 3 Line breaks {#Line-breaks}

#### 3.1 Line length {#Line-length}

In Teletext, which is used to display subtitles on some broadcast platforms, line length is limited to 37 fixed-width (monospaced) characters, since at least 3 of the 40 available bytes are used for control codes. Other platforms use proportional
fonts, making it impossible to determine the width of the line based on the number of characters alone. In this case, lines are constrained by the width of the region in which they are displayed. Guidelines for both platforms are summarised
in the table below.

If targeting both online and broadcast platforms you must apply both constraints, i.e. ensure that the number of characters within a region does not exceed 37.

<table>
<colgroup>
<col style="width: 18%;">
<col style="width: 35%;">
<col>
</colgroup>
<thead>
<tr>
<th scope="col" style="padding: 2px; border: 1px solid rgb(153, 153, 153);">
<p style="margin: 0px;"><strong style="font-weight: bold;">Platform</strong></p>
</th>
<th scope="col" style="padding: 2px; border: 1px solid rgb(153, 153, 153);">
<p style="margin: 0px;"><strong>Max length</strong></p>
</th>
<th scope="col" style="padding: 2px; border: 1px solid rgb(153, 153, 153);">
<p style="margin: 0px;"><strong style="font-weight: bold;">Notes</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding: 2px; border: 1px solid rgb(153, 153, 153);">
<p style="margin: 0px;"><u class="flag-broadcast">broadcast</u></p>
</td>
<td style="padding: 2px; border: 1px solid rgb(153, 153, 153);">
<p style="margin: 0px;">37 characters, reduced if coloured text is used
</p>
</td>
<td style="padding: 2px; border: 1px solid rgb(153, 153, 153);">
Teletext constraint</td>
</tr>
<tr>
<td style="padding: 2px; border: 1px solid rgb(153, 153, 153);">
<p style="margin: 0px;"><u class="flag-online">online</u></p>
</td>
<td style="padding: 2px; border: 1px solid rgb(153, 153, 153);">
<p style="margin: 0px;">68% of the width of a landscape 16:9 video;</p>
<p style="margin: 0px;">90% of the width of a 4:3 video;</p>
<p style="margin: 0px;">90% of the width of a square 1:1 video;</p>
<p style="margin: 0px;">90% of the width of a vertical 9:16 video.</p>
</td>
<td style="padding: 2px; border: 1px solid rgb(153, 153, 153);">
<p>The number of characters that generate this width is determined by the font used,
the given font size (see <a href="#Fonts">fonts</a>) and
the width of the characters in the particular piece of text (for example, 'lilly' takes
up less width than 'mummy' even though both contain the same number of characters).</p>
<p>As a guide, the equivalent to 37 characters in a 75% width region of a 16:9 (landscape) video is
25 characters in a 90% width region of a 9:16 (vertical) video.
Using a proportionally spaced font,
it may be possible to fit a few more characters in,
especially narrow ones like 'i' or 'l'
but if there a lot of wide characters like 'w' or 'm' then
even 25 characters might not fit.</p>
</td>
</tr>
</tbody>
</table>

<aside aria-description="Developer information">

</aside>

#### 3.2 Subtitles should contain single sentences {#Subtitles-should-contain-single-sentences}

Each subtitle should comprise a single complete sentence. Depending on the speed of speech, there are exceptions to this general recommendation (see [live
subtitling](#live-subtitling), short and long sentences below)

#### 3.3 Number of lines {#Number-of-lines}

For landscape or square (16:9, 4:3 or 1:1) video, a maximum subtitle length of two lines is recommended.

For vertical (9:16) video, a maximum subtitle length of three lines is recommended.

Extra lines may be used if you are confident that no important picture information will be obscured.

When deciding between one long line or two short ones,
consider line breaks, number of words, pace of speech and the image.

<aside aria-description="Developer information">
A region sized to fit 3 lines at a recommended computed value of line height of 8% of the height of the root container region would have a minimum extent height of 24%.
</aside>

#### 3.4 Break at natural points {#Break-at-natural-points}

Subtitles and lines should be broken at logical points. The ideal line-break will be at a piece of punctuation like a full stop, comma or dash. If the break has to be elsewhere in the sentence, avoid splitting the following parts of speech:
- article and noun (e.g. the + table; a + book)
- preposition and following phrase (e.g. on + the table; in + a way; about + his life)
- conjunction and following phrase/clause (e.g. and + those books; but + I went there)
- pronoun and verb (e.g. he + is; they + will come; it + comes)
- parts of a complex verb (e.g. have + eaten; will + have + been + doing)

However, since the dictates of space within a subtitle are more severe than between subtitles, line breaks may also take place after a verb. For example:

<samp class="example">We are aiming to
get<br>
a better television service.</samp>

Line endings that break up a closely integrated phrase should be avoided where possible.

<samp class="example"><s>We are aiming to get a<br>
better television service.</s></samp>

Line breaks within a word are especially disruptive to the reading process and should be avoided. Ideal formatting should therefore compromise between linguistic and geometric considerations but with priority given to linguistic considerations.

<aside aria-description="Developer information">
Manual line breaks within paragraphs are specified using line break elements. Automatic line breaks occur between adjacent active paragraph elements.
</aside>

#### 3.5 Breaks in justified subtitles {#Breaks-in-justified-subtitles}

<u class="flag-broadcast">broadcast</u> Left, right and centre justification can be useful to identify speaker position, especially in cases where there are more than three speakers on screen. In such cases, line breaks should be inserted
at linguistically coherent points, taking eye-movement into careful consideration. For example:

<samp class="example">We all hope<br>
you are feeling much better.</samp>

This is left justified. The eye has least distance to travel from ‘hope’ to ‘you’.

<samp class="example">We all hope you
are<br>
feeling much better.</samp>

This is centre justified. The eye now has least distance to travel from ‘are’ to ‘feeling’.

Problems occur with justification when a short sentence or phrase is followed by a longer one.

<samp class="example">Oh.<br>
He didn’t tell me you would be here.</samp>

In this case, there is a risk that the bottom line of the subtitle is read first.

<samp class="example">Oh.<br>
He didn’t tell me you would be here.</samp>

This could result in only half of the subtitle being read.

Allowances would therefore have to be made by breaking the line at a linguistically non-coherent point:

<samp class="example">Oh. He didn’t tell
me<br>
you would be here.</samp>

<samp class="example">Oh. He didn’t tell
me you would be<br>
here.</samp>

<aside aria-description="Developer information">
Left, centre and right justification can be specified using text alignment; additional alignment options are available using multi-row alignment.
</aside>

#### 3.6 Consider the image {#Consider-the-image}

When making a choice between one long line or two short lines, you should consider the background picture. In general, ‘long and thin’ subtitles are less disruptive of picture content than are ‘short and fat’ subtitles, but this is not always
the case. Also take into account the number of words, line breaks etc.

#### 3.7 Consider speaker positioning {#Consider-speaker-positioning}

<u class="flag-broadcast">broadcast</u> In dialogue sequences it is often helpful to use horizontal displacement in order to distinguish between different speakers. ‘Short and fat’ subtitles permit greater latitude for this technique.

#### 3.8 Short sentences {#Short-sentences}

Short sentences may be combined into a single subtitle if the available reading time is limited. However, you should also consider the image and the action on screen. For example, consecutive subtitles may reflect better the pace of speech.

#### 3.9 Long sentences {#Long-sentences}

In most cases verbatim subtitles are preferred to edited subtitles (see this [research by BBC R&D](https://www.bbc.co.uk/rd/blog/2015-09-how-fast-should-subtitles-be)) so avoid breaking long sentences into two shorter sentences.
Instead, allow a single long sentence to extend over more than one subtitle. Sentences should be segmented at natural linguistic breaks such that each subtitle forms an integrated linguistic unit. Thus, segmentation at clause boundaries
is to be preferred. For example:

<samp class="example">When I jumped on
the bus</samp>

<samp class="example">I saw the man who
had taken<br>
the basket from the old lady.</samp>

Segmentation at major phrase boundaries can also be accepted as follows:

<samp class="example">On two minor
occasions<br>
immediately following the war,</samp>

<samp class="example">small numbers of
people<br>
were seen crossing the border.</samp>

There is considerable evidence from the psycho-linguistic literature that normal reading is organised into word groups corresponding to syntactic clauses and phrases, and that linguistically coherent segmentation of text can significantly
improve readability.

Random segmentation must certainly be avoided:

<samp class="example"><s>On two minor
occasions<br>
immediately following the war, small</s></samp>

<samp class="example"><s>numbers of people,
etc.</s></samp>

In the examples given above, no markers are used to indicate that segmentation is taking place. It is also acceptable to use sequences of dots (three at the end of a to-be-continued subtitle, and two at the beginning of a continuation) to
mark the fact that a segmentation is taking place, especially in legacy subtitle files.

<aside aria-description="Developer information">
Because line breaks require considering all of the above, they are better inserted manually. Implementers should avoid automatic line breaking. See the [tts:wrapOption](#tts-wrapOption) XML attribute.
</aside>

#### 3.10 Prioritise editing and timing over line breaks {#Prioritise-editing-and-timing-over-line-breaks}

Good line-breaks are extremely important because they make the process of reading and understanding far easier. However, it is not always possible to produce good line-breaks as well as well-edited text and good timing. Where these constraints
are mutually exclusive, then well-edited text and timing are more important than line-breaks.

### 4 Timing {#Timing}

The recommended subtitle speed is 160-180 words-per-minute (WPM) or 0.33 to 0.375 second per word. However, viewers tend to prefer verbatim subtitles, so the rate may be adjusted to match the pace of the programme. Most subtitle authoring
tools calculate the WPM and can be configured to give a warning when the word rate exceeds a certain WPM threshhold. You can also calculate the WPM manually (see box).

<aside aria-description="Developer information">
To calculate the word-per-minute (WPM) speed of a subtitle, divide the number of words by its duration. For example, a 2-word subtitle displayed for 1 second has a word rate of 120 WPM.
```
<p xml:id="subtitle1" region="bottomRegion" style="paragraphStyle"
begin="00:00:02" end="00:00:04">
 <span style="spanStyle">one, two...</span>
</p>
<p>
 <span style="spanStyle" begin="00:01:30" end="00:01:35">three...</span>
 <span style="spanStyle" begin="00:01:33" end="00:01:35">Four!</span>
</p>
```
</aside>

#### 4.1 Target minimum timing {#Target-minimum-timing}

Based on the recommended rate of 160-180 words per minute, you should aim to leave a subtitle on screen for a minimum period of around 0.3 seconds per word (e.g. 1.2 seconds for a 4-word subtitle). However, timings are ultimately an editorial
decision that depends on other considerations, such as the speed of speech, text editing and shot synchronisation. When assessing the amount of time that a subtitle needs to remain on the screen, think about much more than the number of
words on the screen; this would be an unacceptably crude approach.

#### 4.2 When to give less time {#When-to-give-less-time}

Do not dip below the target timing unless there is no other way of getting round a problem. Circumstances which could mean giving less reading time are:

##### 4.2.1 Shot changes {#Shot-changes}

Give less time if the target timing would involve clipping a shot, or crossing into an unrelated, "empty" [containing no speech] shot. However, always consider the alternative of merging with another subtitle.

##### 4.2.2 Lip reading {#Lip-reading}

Give less time to avoid editing out words that can be lip-read, but only in very specific circumstances: i.e. when a word or phrase can be read very clearly even by non-lip-readers, and if it would look ridiculous to take out or change the
word.

##### 4.2.3 Catchwords {#Catchwords}

Avoid editing out catchwords if a phrase would become unrecognisable if edited.

##### 4.2.4 Retaining humour {#Retaining-humour}

Give less time if a joke would be destroyed by adhering to the standard timing, but only if there is no other way around the problem, such as merging or crossing a shot.

##### 4.2.5 Critical information {#Critical-information}

In a news item or factual content, the main aim is to convey the "what, when, who, how, why". If an item is already particularly concise, it may be impossible to edit it into subtitles at standard timings without losing a crucial element of
the original.

##### 4.2.6 Very technical items {#Very-technical-items}

These may be similarly hard to edit. For instance, a detailed explanation of an economic or scientific story may prove almost impossible to edit without depriving the viewer of vital information. In these situations a subtitler should be prepared
to vary the timing to convey the full meaning of the original.

#### 4.3 When to give extra time {#When-to-give-extra-time}

Try to allow extra reading time for your subtitles in the following circumstances:

##### 4.3.1 Unfamiliar words {#Unfamiliar-words}

Try to give more generous timings whenever you consider that viewers might find a word or phrase extremely hard to read without more time.

##### 4.3.2 Several speakers {#Several-speakers}

Aim to give more time when there are several speakers in one subtitle.

##### 4.3.3 Labels {#Labels}

Allow an extra second for labels where possible, but only if appropriate.

##### 4.3.4 Visuals and graphics {#Visuals-and-graphics}

When there is a lot happening in the picture, e.g. a football match or a map, allow viewers enough time both to read the subtitle and to take in the visuals.

##### 4.3.5 Placed subtitles {#Placed-subtitles}

If, for example, two speakers are placed in the same subtitle, and the person on the right speaks first, the eye has more work to do, so try to allow more time.

##### 4.3.6 Long figures {#Long-figures}

Give viewers more time to read long figures (e.g. 12,353).

##### 4.3.7 Shot changes {#Shot-changes-2}

Aim for longer timing if your subtitle crosses one shot or more, as viewers will need longer to read it.

##### 4.3.8 Slow speech {#Slow-speech}

Slower timings should be used to keep in sync with slow speech.

#### 4.4 Use consistent timing {#Use-consistent-timing}

It is also very important to keep your timings consistent. For instance, if you have given 3:12 for one subtitle, you must not then give 4:12 to subsequent subtitles of similar length - unless there is a very good reason: e.g. slow speaker/on-screen
action.

#### 4.5 Gaps {#Gaps}

If there is a pause between two pieces of speech, you may leave a gap between the subtitles - but this must be a minimum of one second, preferably a second and a half. Anything shorter than this produces a very jerky effect. Try to not squeeze
gaps in if the time can be used for text.

### 5 Synchronisation {#Synchronisation}

#### 5.1 Match subtitle to speech onset {#Match-subtitle-to-speech-onset}

Impaired viewers make use of visual cues from the faces of television speakers. Therefore subtitle appearance should coincide with speech onset. Subtitle disappearance should coincide roughly with the end of the corresponding speech segment,
since subtitles remaining too long on the screen are likely to be re-read by the viewer.

When two or more people are speaking, it is particularly important to keep in sync. Subtitles for new speakers must, as far as possible, come up as the new speaker starts to speak. Whether this is possible will depend on the action on screen
and rate of speech.

The same rules of synchronisation should apply with off-camera speakers and even with off-screen narrators, since viewers with a certain amount of residual hearing make use of auditory cues to direct their attention to the subtitle area.

#### 5.2 Match subtitle to pace of speaking {#Match-subtitle-to-pace-of-speaking}

The subtitles should match the pace of speaking as closely as possible. Ideally, when the speaker is in shot, your subtitles should not anticipate speech by more than 1.5 seconds or hang up on the screen for more than 1.5 seconds after speech
has stopped.

However, if the speaker is very easy to lip-read, slipping out of sync even by a second may spoil any dramatic effect and make the subtitles harder to follow. The subtitle should not be on the screen after the speaker has disappeared.

Note that some decoders might override the end timing of a subtitle so that it stays on screen until the next one appears. This is a non-compliant behaviour that the subtitle author and broadcaster have no control over.

<aside aria-description="Developer information">
Decoders need to match the begin and end timing specified in documents as closely as possible to maintain the careful synchronisation we expect from subtitle authors. Timing precision is especially important when video is presented at low frame rates.
</aside>

#### 5.3 Display subtitles when lips are moving {#Display-subtitles-when-lips-are-moving}

A subtitle (or an explanatory label) should always be on the screen if someone's lips are moving. If a speaker speaks very slowly, then the subtitles will have to be slow, too - even if this means breaking the timing conventions. If a speaker
speaks very fast, you have to edit as much as is necessary in order to meet the timing requirements (see [timing](#Timing)).

#### 5.4 Keep lag behind speech to a minimum {#Keep-lag-behind-speech-to-a-minimum}

Your aim is to minimise lag between speech and the appearance of the subtitle. But sometimes, in order to meet other requirements (e.g. matching shots), you will find it difficult to avoid slipping slightly out of sync. In this case, subtitles
should never appear more than 2 seconds after the words were spoken. This should be avoided by editing the previous subtitles.

It is permissible to slip out of sync when you have a sequence of subtitles for a single speaker, providing the subtitles are back in sync by the end of the sequence.

If the speech belongs to an out-of-shot speaker or is voice-over commentary, then it's not so essential for the subtitles to keep in sync.

#### 5.5 Do not pre-empt an effect {#Do-not-pre-empt-an-effect}

Do not bring in any dramatic subtitles too early. For example, if there is a loud bang at the end of, say, a two-second shot, do not anticipate it by starting the label at the beginning of the shot. Wait until the bang actually happens, even
if this means a fast timing.

#### 5.6 Keep speakers separate {#Keep-speakers-separate}

Do not simultaneously caption different speakers if they are not speaking at the same time.

### 6 Matching shots {#Matching-shots}

#### 6.1 Match subtitles to shot {#Match-subtitles-to-shot}

It is likely to be less tiring for the viewer if shot changes and subtitle changes occur at the same time. Many subtitles therefore start on the first frame of the shot and end on the last frame.

#### 6.2 Maintain a minimum gap when mismatched {#Maintain-a-minimum-gap-when-mismatched}

If you have to let a subtitle hang over a shot change, do not remove it too soon after the cut. The duration of the overhang will depend on the content.

#### 6.3 Avoid straddling shot changes {#Avoid-straddling-shot-changes}

Avoid creating subtitles that straddle a shot change (i.e. a subtitle that starts in the middle of shot one and ends in the middle of shot two). To do this, you may need to split a sentence at an appropriate point, or delay the start of a
new sentence to coincide with the shot change.

<aside aria-description="Developer information">
Authoring tools may use automated shot detection to avoid this scenario.
</aside>

#### 6.4 Merge subtitles for short shots {#Merge-subtitles-for-short-shots}

If one shot is too fast for a subtitle, then you can merge the speech for two shots – provided your subtitle then ends at the second shot change.

Bear in mind, however, that it will not always be appropriate to merge the speech from two shots: e.g. if it means that you are thereby "giving the game away" in some way. For example, if someone sneezes on a very short shot, it is more effective
to leave the "Atchoo!" on its own with a fast timing (or to merge it with what comes afterwards) than to anticipate it by merging with the previous subtitle.

#### 6.5 End subtitle with speech {#End-subtitle-with-speech}

Where possible, avoid extending a subtitle into the next shot when the speaker has stopped speaking, particularly if this is a dramatic reaction shot.

#### 6.6 End subtitle with scene {#End-subtitle-with-scene}

Never carry a subtitle over into the next shot if this means crossing into another scene or if it is obvious that the speaker is no longer around (e.g. if they have left the room).

#### 6.7 Wait for scene change to subtitle speaker {#Wait-for-scene-change-to-subtitle-speaker}

Some film techniques introduce the soundtrack for the next scene before the scene change has occurred. If possible, the subtitler should wait for the scene change before displaying the subtitle. If this is not possible, the subtitle should
be clearly labelled to explain the technique.

<samp class="example">JOHN: And what have
we here?</samp>

### 7 Identifying speakers {#Identifying-speakers}

Several techniques can be used to assist the viewer in identifying speakers. The BBC's preferred techniques are colour and single quotes, but other techniques exist in legacy subtitle files and subtitles repurposed from non-UK sources. Re-use
of existing files with legacy techniques is acceptable, but unless specifically requested, new content should not use legacy techniques.

The available techniques include:
- [Colour](#Use-colours): This is the preferred method that should be used in most cases.
- [Single quotes](#Use-single-quotes-for-voice-over): Used to indicate an out-of-vision speaker, such as someone speaking via telephone, or to distinguish between in- and out-of-vision voices when both are spoken by the same character
(or by the narrator) and therefore using the same colour (e.g. a narrator who is sometimes in-vision).
- [Arrows](#Use-arrows-for-off-screen-voices): Used to indicate the direction of out-of-vision sounds when the origin of the sound is not apparent. (infrequently used)
- [Label](#Use-labels-for-off-screen-voices): Can be used to resolve ambiguity as to who is speaking.
- [Horizontal
positioning](#Use-horizontal-positioning): This is a legacy technique for identifying in-vision speakers, but it is still used for indicating [off-screen speech](#Use-arrows-for-off-screen-voices). It is also used with [Vertical
positioning](#Vertical-positioning) to avoid obscuring important information.
- [Dashes](#Use-dashes): This is a legacy technique. Must only be used with colour when unavoidable.

#### 7.1 Use colours {#Use-colours}

Use colours to distinguish speakers from each other (see
[Colours](#Colours)). This is the preferred method for identifying speakers.

Where the speech for two or more speakers of different colours is combined in one subtitle, their speech runs on: i.e. you don't start a new line for each new speaker.

<samp class="example"><span style="color:yellow;">Did you see Jane?</span> I thought she went home.
</samp>

However, if two or more WHITE text speakers are interacting, you have to start a new line for each new speaker, preceded by a dash.

By convention, the narrator is indicated by a yellow colour.

<aside aria-description="Developer information">
Colour is implemented using color property and span.
</aside>

#### 7.2 Use horizontal positioning {#Use-horizontal-positioning}

*This is a legacy technique that is no longer used in new
content for identifying in-vision speakers (it may be present in
files created before it was deprecated). Use colour
instead.*

Horizontal positioning is used in combination with arrows to indicate out-of-vision voices.

<u class="flag-broadcast">broadcast</u> Where colours cannot be used you can distinguish between speakers with placing.

Put each piece of speech on a separate line or lines and place it underneath the relevant speaker. You may have to edit more to ensure that the lines are short enough to look placed.

Try to make sure that pieces of speech placed right and left are "joined at the hip" if possible, so that the eye does not have to leap from one side of the screen to the other.

<img src="/accessibility/forproducts/guides/subtitles/img/8.2-1.png" alt="Two lines of subtitles overlapping horizontally.">

Not:

<img src="/accessibility/forproducts/guides/subtitles/img/8.2-2.png" alt="Two lines of subtitles with no overlap.">

When characters move about while speaking, the caption should be positioned at the discretion of the subtitler to identify the position of the speaker as clearly as possible.

<aside aria-description="Developer information">
Horizontal positioning is determined by text direction and alignment properties.
- [tts:writingMode](#tts-writingMode)
</aside>

#### 7.3 Use dashes {#Use-dashes}

*This is a legacy technique that is no longer used for new
content (but may be present in files created before it was
deprecated or sourced from outside the UK). Use colour to indicate
a change of speaker.*

If colour cannot be used (or if colour is being used but two consecutive speakers are both assigned the same colour), put each piece of speech on a separate line and insert a white dash (not a hyphen) before each piece of speech, thereby clearly
distinguishing different speakers' lines. If possible, align the dashes so that they are proud of the text, although not all formats support this well.

<samp class="example">– Found anything?<br>
– If this is the next new weapon,<br>
we're in big trouble.</samp>

The longest line should be centred on the screen, with the shorter line/lines left-aligned with it (not centred). If one of the lines is long, inevitably all the text will be towards the left of the screen, but generally the aim is to keep
the lines in the centre of the screen.

Note that dashes only work as a clear indication of speakers when each speaker is in a separate consecutive shot.

#### 7.4 Use single quotes for voice-over {#Use-single-quotes-for-voice-over}

If you need to distinguish between an in-vision speaker and a voice-over speaker, use single quotes for the voice-over, but only when there is likely to be confusion without them (single quotes are not normally necessary for a narrator, for
example). Confusion is most likely to arise when the in-vision speaker and the voice-over speaker are the same person.

Put a single quote-mark at the beginning of each new subtitle (or segment, in live), but do not close the single quotes at the end of each subtitle/segment - only close them when the person has finished speaking, as is the case with paragraphs
in a book.

<samp class="example">'I've lived in the
Lake District since I was a boy.</samp>

<samp class="example">'I never want to
leave this area.<br>
I've been very happy here.</samp>

<samp class="example">'I love the fresh
air and the beautiful scenery.'</samp>

If more than one speaker in the same subtitle is a voice-over, just put single quotes at the beginning and end of the subtitle.

<samp class="example"><span style="color:yellow;">'What do you think about it?</span> I'm not sure.'
</samp>

The single quotes will be in the same colour as the adjoining text.

#### 7.5 Use single quotes for out-of-vision speaker {#Use-single-quotes-for-out-of-vision-speaker}

When two white text speakers are having a telephone conversation, you will need to distinguish the speakers. Using single quotes placed around the speech of the out-of-vision speaker is the recommended approach. They should be used throughout
the conversation, whenever one of the speakers is out of vision.

<samp class="example">Hello. Victor
Meldrew speaking.<br>
'Hello, Mr Meldrew. I'm calling about your car.'</samp>

Single quotes are not necessary in telephone conversations if the out-of-vision speaker has a colour.

#### 7.6 Use double quotes for mechanical speech and for quoting {#Use-double-quotes-for-mechanical-speech-and-for-quoting}

Double quotes "..." can suggest mechanically reproduced speech, e.g. radio, loudspeakers etc., or a quotation from a person or book. Start the quote with a capital letter:

<samp class="example">He said, "You're so tall".</samp>

#### 7.7 Use arrows for off-screen voices {#Use-arrows-for-off-screen-voices}

Generally, colours should be used to identify speakers. However, when an out-of-shot speaker needs to be distinguished from an in-shot speaker of the same colour, or when the source of off-screen/off-camera speech is not obvious from the visible
context, insert a ‘greater than’ (>) or ‘less than’ (<) symbols to indicate the off-camera speaker.

If the out-of-shot speaker is on the left or right, type a left or right arrow (< or >) next to their speech and place the speech to the appropriate side. Left arrows go immediately before the speech, followed by one space; right
arrows immediately after the speech, preceded by one space.

<samp class="example">Do come in.<br>
<span style="color:yellow;">Are you sure?</span> &gt;</samp>

<samp class="example">When are you
leaving?<br>
&lt; <span style="color:yellow;">I was thinking of going<br>
at around 8 o'clock in the evening.</span></samp>

<samp class="example">When I find out
where he is,&nbsp;&nbsp;&nbsp;<br>
you'll be the first to know. &gt;</samp>

NOT:

<samp class="example"><s>When I find out where he is,
&gt;<br>
you'll be the first to know.</s></samp>

If possible, make the arrow clearly visible by keeping it clear of any other lines of text, i.e. the text following the arrow and the text in any lines below it are aligned. However, not all formats support hanging indent well.

<aside aria-description="Developer information">
The `<` and `>`
characters are not permitted directly

See [Encoding characters](#Encoding-characters)
for information about how to escape them correctly.
</aside>

<aside aria-description="Developer information">
Non-breaking spaces can be inserted to simulate the indent behaviour reasonably closely.
</aside>

<samp class="example">&lt; When I find out
where he is,<br>
&nbsp;&nbsp;&nbsp;you'll be the first to know</samp>

The arrows are always typed in white regardless of the text colour of the speaker.

If an off-screen speaker is neither to the right nor the left, but straight ahead, do not use an arrow.

<u class="flag-online">online</u> Arrow characters (← and →) can be used instead of < and > for online-only subtitles.

#### 7.8 Use labels for off-screen voices {#Use-labels-for-off-screen-voices}

If you are unable to use any other technique, use a label to identify a speaker, but only if it is unclear who was speaking or when more than four characters are speaking, requiring a shared colour. Type the name of the speaker in white caps
(regardless of the colour of the speaker's text), immediately before the relevant speech.

If there is time, place the speech on the line below the label, so that the label is as separate as possible from the speech. If this is not possible, put the label on the same line as the speech, centred in the usual way.

<samp class="example">JAMES:<br>
What are you doing with that hammer?</samp>

<samp class="example">JAMES: What are you
doing?</samp>

If you do not know the name of the speaker, indicate the gender or age of the speaker if this is necessary for the viewer's understanding:

<samp class="example">MAN: I was brought up
in a close-knit family.</samp>

When two or more people are speaking simultaneously, do the following, regardless of their colours:

Two people:

<samp class="example">BOTH: Keep
quiet!</samp> (all white text)

Three or more:

<samp class="example">ALL: Hello!</samp> (all white text)

<samp class="example">TOGETHER:
<span style="color:yellow;">Yes!</span> No!</samp> (different colours with a white label)

#### 7.9 Use metadata to identify speakers {#Use-metadata-to-identify-speakers}

The subtitle file formats used by the BBC allow non-presentation metadata that can be used to include information about the speaker of a subtitle. Including this information is useful for searching, identifying speakers and other purposes.

<aside aria-description="Developer information">
Speakers can be identified using the `ttm:agent` attribute defined in the `tt/head/metadata` element and [referenced](#Element-references-and-xml-id-attributes) by a
span element. This should be used wherever possible in documents and may be removed from documents prior to distribution,
if the data is not needed by the presentation processor.
</aside>

### 8 Colours {#Colours}

#### 8.1 Use white on black {#Use-white-on-black}

Most subtitles are typed in white text on a black background to ensure optimum legibility.

See [Stress](#Stress) for the single case where colour may be used for emphasis.

<aside aria-description="Developer information">
Colours are implemented using color property and [tts:backgroundColor](#tts-backgroundColor) [applied](#Applying-style-attributes-to-content-elements) to a
span.
Where two words are in different colours the space must be placed within one of the span elements, usually as the first character of the second span.
</aside>

#### 8.2 Avoid coloured background {#Avoid-coloured-background}

Background colours are no longer used. Use labels to identify non-human speakers:

<samp class="example">ROBOT: Hello,
sir</samp>

Use left-aligned sound labels for alerts:

<samp class="example">BUZZER</samp>

#### 8.3 Speaker colours {#Speaker-colours}

A limited range of colours can be used to distinguish speakers from each other. In order of priority:

<table>
<colgroup>
<col style="width: 20%;">
<col style="width: 20%;">
<col>
</colgroup>
<thead>
<tr>
<th scope="col">
<p><strong>Colour</strong></p>
</th>
<th scope="col">
<p><strong>RGB hex</strong></p>
</th>
<th scope="col">
<p><strong>Notes</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p>White</p>
</td>
<td>
<p><code>#FFFFFF</code></p>
</td>
<td></td>
</tr>
<tr>
<td>
<p>Yellow</p>
</td>
<td>
<p><code>#FFFF00</code></p>
</td>
<td></td>
</tr>
<tr>
<td>
<p>Cyan</p>
</td>
<td>
<p><code>#00FFFF</code></p>
</td>
<td></td>
</tr>
<tr>
<td>
<p>Green</p>
</td>
<td>
<p><code>#00FF00</code></p>
</td>
<td>

</td>
</tr>
</tbody>
</table>

All of the above colours must appear on a black background to ensure maximum legibility.

#### 8.4 Apply speaker colour consistently {#Apply-speaker-colour-consistently}

Once a speaker has a colour, they should keep that colour. Avoid using the same colour for more than one speaker - it can cause a lot of confusion for the viewer.

The exception to this would be content with a lot of shifting main characters like EastEnders, where it is permissible to have two characters per colour, providing they do not appear together. If the amount of placing needed would mean editing
very heavily, you can use green as a "floater": that is, it can be used for more than one minor character, again providing they never appear together.

#### 8.5 Multiple speakers in white {#Multiple-speakers-in-white}

White can be used for any number of speakers. If two or more white speakers appear in the same scene, you have to use one of a number of devices to indicate who says what - see [Identifying Speakers](#Identifying-speakers).

### 9 Typography {#Typography}

#### 9.1 Fonts {#Fonts}

Subtitle fonts are determined by the platform, the delivery mechanism and the client as detailed below. Since fonts have different character widths, the final pixel width of a line of subtitles cannot be accurately determined when authoring.
See also [Line Breaks](#Line-breaks).

To minimise the risk of unwanted line wrapping, use a wide font such as Reith Sans, Verdana or Tiresias when authoring the subtitles.
 Presentation processors usually use a narrower font (e.g. Arial) so the rendered line will likely fit within the authored area.
 Note that platforms may use different reference fonts when resolving the generic font family name specified in the subtitle file.
 For example, the HbbTV standard maps both `default` and
 `proportionalSansSerif` to Tiresias,
 whereas IMSC maps `proportionalSansSerif` only to any font with
 substantially the same dimensions for rendered text as Arial.
 See also [Conformance with IMSC 1.0.1 Text Profile](#Conformance-with-IMSC-1-0-1-Text-Profile).

<table>
<colgroup>
<col style="width: 18%;">
<col style="width: 18%;">
<col>
</colgroup>
<thead>
<tr>
<th scope="col">
<p><strong>Platform</strong></p>
</th>
<th scope="col">
<p><strong>Delivery</strong></p>
</th>
<th scope="col">
<p><strong>Description</strong></p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<p><u class="flag-broadcast">broadcast</u></p>
</td>
<td>
<p>DVB</p>
</td>
<td>The subtitle encoder creates bitmap images for each subtitle using the Tiresias Screenfont font</td>
</tr>
<tr>
<td>
<p><u class="flag-broadcast">broadcast</u></p>
</td>
<td>
<p>Teletext</p>
</td>
<td>The set top box or television determines the font - this is most commonly used on the Sky platform</td>
</tr>
<tr>
<td>
<p><u class="flag-online">online</u></p>
</td>
<td>
<p>IP (XML)</p>
</td>
<td>The client determines the font using information from within the subtitle data (e.g. 'SansSerif'). Generally it is better to use system font for readability (e.g. Helvetica for iOS and Roboto for Android). Use of non-platform fonts
can adversely impact clarity of presented text.</td>
</tr>
</tbody>
</table>

<aside aria-description="Developer information">
For implementation details, see [tts:fontFamily](#tts-fontFamily).
</aside>

#### 9.2 Size {#Size}

The final displayed size of closed captions text is determined by multiple factors: the instructions in the subtitle file, the processor and the set of installed fonts available to it, the device screen size and resolution and (on some devices)
also user-defined preferences.

While it is not possible (or advisable) to pre-determine the final subtitle size, adhering to the below guidelines will ensure that subtitles are legible at a typical distance from the device and that lines do not reflow or overflow for the
vast majority of users. In particular, the final size should never be larger than the authored size so that the subtitler can ensure that important parts of the of the video are not obscured.

##### 9.2.1 Authoring font size {#Authoring-font-size}

Font size should be set to fit within a line height in the range 7% to 8% of
the active video height for 16:9, 4:3 and 1:1 aspect ratio videos,
for example a computed line height of 7.5% would be acceptable.

Font size should be set to fit within a line height in the range 3.9% to 4.5% of
the active video height for 9:16 aspect ratio videos,
for example a computed line height of 4.2% would be acceptable.

This font height is the largest size needed for presentation and is an *authoring* requirement.

<img src="/accessibility/forproducts/guides/subtitles/img/10.2-2.png" alt="Image showing line height being 8% of active video height, character height being sized to fit">

Use a wide font such as Reith Sans when authoring subtitles (see [Fonts](#Fonts) and [tts:fontFamily](#tts-fontFamily)).
If that is not the font used to present it, then the alternative is likely to be a narrower font, so if you author
in a wide font you can be reasonably confident that lines will not reflow.

No changes need to be made to other styling attributes to accommodate processors potentially using a smaller font, however care needs to be taken when positioning subtitles in case a smaller font is used, as the following examples show:

Authored font size, correct positioning:

<img src="/accessibility/forproducts/guides/subtitles/img/resized_text_1_1.png" alt="A mock-up of a head and shoulders shot with a caption along the bottom, with a two line subtitle avoiding the face, with large sized text tightly surrounded by a rectangle that indicates the region and overlaps with the face.">

The processor displays the larger font size, as authored. The region (not displayed) is indicated with a dotted line.

Reduced font size, wrong positioning:

<img src="/accessibility/forproducts/guides/subtitles/img/resized_text_1_2.png" alt="A mock-up of a head and shoulders shot with a caption along the bottom, with a two line subtitle partially obscuring the face, with small sized text aligned to the top of a surrounding rectangle indicating the region, which overlaps with the face.">

The region's `tts:displayAlign` is set to "before" so with a smaller font size the text moves up and the second line obscures the mouth.

Reduced font size, correct positioning:

<img src="/accessibility/forproducts/guides/subtitles/img/resized_text_1_3.png" alt="A mock-up of a head and shoulders shot with a caption along the bottom, with a two line subtitle avoiding the face, with small sized text aligned to the vertical centre of a surrounding rectangle indicating the region, which overlaps with the face.">

To avoid this, set the region's
`tts:displayAlign` property to "center" or "after".

Authored font size, large region:

<img src="/accessibility/forproducts/guides/subtitles/img/resized_text_2_1.png" alt="A mock-up of a head and shoulders shot with a caption along the bottom, with a two line subtitle avoiding the face, with large sized text positioned using &lt;br&gt; elements in a much larger rectangle that indicates the region and overlaps with the face.">

Line breaks were used to position the subtitles lower within the region.

Reduced font size, large region:

<img src="/accessibility/forproducts/guides/subtitles/img/resized_text_2_2.png" alt="A mock-up of a head and shoulders shot with a caption along the bottom, with a two line subtitle partially obscuring the face, with small sized text positioned using &lt;br&gt; elements in a much larger rectangle that indicates the region and overlaps with the face.">

The line breaks are resized with the rest of the text.

Reduced font size, defined region:

<img src="/accessibility/forproducts/guides/subtitles/img/resized_text_2_3.png" alt="A mock-up of a head and shoulders shot with a caption along the bottom, with a three line subtitle avoiding the face, with small sized text positioned within a rectangle that indicates the region, where the rectangle does not overlap with the face.">

Better to define the region so that it does not cover the face and avoid white space.

<aside aria-description="Developer information">
The font size is determined by [tts:fontSize](#tts-fontSize)
in combination with [ttp:cellResolution](#ttp-cellResolution).
The line height is determined by line height
and is relative to the font size of the element on which the line height is set.
The 8% value originates in Teletext,
where it is approximately the height of a double height line,
with the Teletext rendering area covering around 90% of the video area height,
as is typical when they are rendered within a safe area which accommodates overscan.
We currently broadcast teletext subtitles on our digital satellite platforms:
in principle, by connecting a television to a set top box using for example a SCART connector
it would still be possible to display subtitles in this way,
though in practice few if any new products are available that support such a mechanism.
The double height line was used instead of a single height line for readability
when commonly used television sizes were much smaller than today's median sizes
(see [BBC R&D White Paper 287 (PDF)](http://downloads.bbc.co.uk/rd/pubs/whp/whp-pdf-files/WHP287.pdf)
for relevant research on this).
The 4.5% value results from adjusting the 8% value as applied to a 16:9 aspect ratio
video for a 9:16 vertical video, i.e. by multiplying it by 9/16,
so that subtitle text is approximately the same size on a landscape video as on a portrait/vertical video;
since text size is proportional to the video height,
8% of a vertical video is much larger than 8% of a landscape video,
when each is rotated to fill the same 16:9 ratio display.
</aside>

##### 9.2.2 Presentation font size {#Presentation-font-size}

Depending on device size, viewing distance, screen resolution etc., a *processor* (such as a player) may choose to reduce (but not to increase) the authored font size so that the final presentation font size is smaller than the authored
font size. For example, on a very large TV the subtitles may appear too large when displayed at the original authored size, so the processor can apply a scaling factor, or a multiplier of less than 1, to the value of `tts:fontSize`.

For most screen sizes, the preferred font size is between 0.6 and 0.8 times the required
[authoring font size](#Authoring-font-size). For small mobile phones (e.g. 4" diagonal screen size) the presentation size should be the unmodified authored font size (i.e. a multiplier of 1).

Along with reading distance, the physical height of the video when displayed on the device's screen is the most direct determinant of font size as a proportion of video height. In practice, however, a processor may not know the actual physical
height and may have to rely on other data, for example pixel size and resolution (which may not be reliable indicators of physical size). The examples below illustrate devices and their recommended multipliers. For devices that support
configurable sizes, a recommended range is shown. When the processor cannot determine the screen size, it should use the unmodified authored size to mitigate the risk of illegibly small text (i.e. default to a multiplier of 1).

<table>
<colgroup>
<col>
<col style="width: 20%;">
<col style="width: 18%;">
<col style="width: 15%;">
<col style="width: 15%;">
</colgroup>
<thead>
<tr>
<th scope="col">Device type</th>
<th scope="col">Example device</th>
<th scope="col">Screen height (landscape)</th>
<th scope="col">Recommended multiplier</th>
<th scope="col">Recommended range</th>
</tr>
</thead>
<tbody>
<tr>
<td>4" (10cm) phone</td>
<td>iPhone SE</td>
<td>50mm</td>
<td>x1</td>
<td>x0.67-x1</td>
</tr>
<tr>
<td>4.7" (12cm) phone</td>
<td>iPhone 6 </td>
<td>59mm</td>
<td>x1</td>
<td>x0.67-x1</td>
</tr>
<tr>
<td>5.5" (14cm) phone</td>
<td>Samsung S7</td>
<td>68mm</td>
<td>x0.67</td>
<td>x0.5-x1</td>
</tr>
<tr>
<td>7" (17.8cm) tablet</td>
<td>Amazon Fire</td>
<td>87mm</td>
<td>x0.8</td>
<td>x0.6-x1</td>
</tr>
<tr>
<td>9.7" (24.5cm) tablet</td>
<td>iPad</td>
<td>148mm</td>
<td>x0.67</td>
<td>x0.6-x1</td>
</tr>
<tr>
<td>Laptop and desktop computers</td>
<td>16:9 monitor</td>
<td>187mm-300mm</td>
<td>x0.6</td>
<td>x0.5-x1</td>
</tr>
<tr>
<td>TVs (32"-42")</td>
<td>16:9 or 21:9 display</td>
<td>398mm-523mm</td>
<td>x0.67</td>
<td>x0.5-x1</td>
</tr>
<tr>
<td>Unknown device</td>
<td>Unknown</td>
<td>Unknown</td>
<td>x1</td>
<td>x0.67-x1</td>
</tr>
</tbody>
</table>

The same multipliers apply regardless of the aspect ratio of the video.
See [Authoring font size](#Authoring-font-size) above for the
size adjustment needed for vertical (9:16) video.

In the absence of other information, a default size of 0.5° subtended at the eye may be used to derive the default line height and calculate the multiplier, however this may be too small for some devices.

<aside aria-description="Developer information">
When scaling down the font size, the processor should respect all other styling attributes. Subtitle text should be scaled by applying the multiplier to the values of
`tts:fontSize` and
</aside>

##### 9.2.3 Additional adjustments for Reith Sans font {#Additional-adjustments-for-Reith-Sans-font}

This section previously contained guidance for adjusting
the line height and font size when presenting using
the Reith Sans font.
That guidance no longer applies due to adjustments
made in versions of the Reith Sans font released
in or after January 2021,
so the contents of this section have been removed.

##### 9.2.4 Background size {#Background-size}

The width of the background is calculated per line, rather than being the largest rectangle that can fit all the displayed lines in.

<aside aria-description="Developer information">
To achieve this, wrap the text in a span and
[apply](#Applying-style-attributes-to-content-elements) a [tts:backgroundColor](#tts:backgroundColor) style to the
span by [referencing](#Element-references-and-xml-id-attributes)
a style element that sets that style attribute.
</aside>

The height of the background should be the height of the line; there should be no gap between background areas of successive lines.

<aside aria-description="Developer information">
[Reference](#Element-references-and-xml-id-attributes) a style element that sets
[itts:fillLineGap="true"](#itts:fillLineGap) from the
paragraph parent, or its
container ancestor,
to instruct the processor to
fill gaps between adjacent line background areas.
</aside>

On both sides of every line, the background colour should extend by the width of 0.5 em.

<img src="/accessibility/forproducts/guides/subtitles/img/10.2-1.png" alt="Image showing background colour calculated per line with no gaps between background areas of consecutive lines.">

<aside aria-description="Developer information">

Note, however, that the size of line padding is expressed in cell units, requiring additional calculation.
For this purpose, `1em` can be assumed to equal font size.
If scaling the presentation font size, a processor should reduce the value of
by the same factor.
</aside>

#### 9.3 Supported characters {#Supported-characters}

##### 9.3.1 Broadcast {#Broadcast}

If the subtitles are intended for broadcast, a limited set of characters must be used.

Use alphanumeric and English punctuation characters:

A-Z a-z 0-9 ! ) ( , . ? : -

The following characters can be used:

> < & @ # % + * = / £ $ ¢ ¥ © ® ¼ ½ ¾ ¾ ™

Do not use accents.

Additional characters are supported but not normally used (see
)

##### 9.3.2 Characters permitted online {#Characters-permitted-online}

In addition to the characters above, the following characters are allowed if the subtitles are intended for online use only.

<u class="flag-online">online</u> € ♫ (replaces # to indicate music) ← → ([arrows](#Use-arrows-for-off-screen-voices) can replace < and >).

Emoji versions of characters,
for example the musical note symbol, 🎵 (U+1F3B5),
must not be used, because they can be hard to see against
a black background. For the musical note, use ♫ (U+266B) instead.

##### 9.3.3 Encoding characters {#Encoding-characters}

<aside aria-description="Developer information">

Special characters may need to be escaped depending on the format:
<table>
<colgroup>
<col style="width: 15%;">
<col style="width: 15%;">
<col>
</colgroup>
<thead>
<tr>
<th scope="col">Character</th>
<th scope="col">Escaped</th>
<th scope="col">Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>&lt;</td>
<td><code>&amp;lt;</code></td>
<td><code>&lt;span style="spanStyle"&gt;3 &amp;lt; 5&lt;/span&gt;</code></td>
</tr>
<tr>
<td>&gt;</td>
<td><code>&amp;gt;</code></td>
<td><code>&lt;span style="spanStyle"&gt;5 &amp;gt; 3&lt;/span&gt;</code></td>
</tr>
<tr>
<td>&amp;</td>
<td><code>&amp;amp;</code></td>
<td><code>&lt;span style="spanStyle"&gt;Trotter &amp;amp; Sons&lt;/span&gt;</code></td>
</tr>
</tbody>
</table>
Quote marks within subtitle content don't have to be escaped. This is valid:
`<span style="spanStyle">"Hello"</span>`
Note, however, that curly quotes are not included in the list of allowed characters (some word processors transform straight quotes to curly ones automatically).
You may not be able directly to key in some of the other
allowed characters. In this case you can use the decimal or
hexadecimal Unicode code. For example, use
`&#9835;`
(which is the decimal code for the character ♫) like this:
`<span style="spanStyle">&#9835; Happy birthday to you</span>`
This will be displayed as:
<samp class="example">♫ Happy birthday to you</samp>
Hexadecimal Unicode character codes can alternatively be
used with the syntax
`&#x266B;`
(decimal `9835` is equal to
hexadecimal `266B`).
You can view [a list of Unicode codes on the Unicode website](https://www.unicode.org/charts/).
</aside>

### 10 Positioning {#Positioning}

The subtitles should overlay the video image,
and may be placed within any black bars present
within the video at the top or bottom.

<u class="flag-online">online</u> For 16:9 video in landscape mode,
subtitles should not be placed outside the central 90% vertically and
the central 75% horizontally.

<u class="flag-online">online</u> For 9:16 video in portrait or vertical mode,
this is reversed: subtitles should not be placed outside the central 75% vertically and
the central 90% horizontally.

<u class="flag-online">online</u> For 4:3 and 1:1 (square) video,
subtitles should not be placed outside the central 90% vertically and
the central 90% horizontally.

<u class="flag-online">online</u> Regions can be extended horizontally
to allow extra space for line padding.

<u class="flag-online">online</u> For online subtitles, the subtitle rendering area
The subtitle display area should exactly overlap the video player area
unless controls or other overlays are visible, in which case the system should
take steps to avoid the subtitles being obscured by the overlays. These could include:
- Scaling the root container to avoid overlap
- Detecting and resolving screen area clashes by moving subtitles around
- Pausing the presentation while the overlays are visible.

#### 10.1 Vertical positioning {#Vertical-positioning}

The normally accepted position for subtitles is towards the bottom of the screen
(Teletext lines 20 and 22. Line 18 is used if three subtitle lines are required).
In obeying this convention it is most important to avoid obscuring ‘on-screen’ captions,
any part of a speaker’s mouth or any other important activity.
Certain special programme types carry a lot of information in the lower part of the screen
(e.g. snooker, where most of the activity tends to centre around the black ball)
and in such cases top screen positioning will be a more acceptable standard.

In vertical (9:16) videos, it is common to position subtitles a little higher up,
though still generally in the lower third of the screen.
This is because faces are generally in the top half of the screen,
and positioning the subtitles at the bottom makes it harder for the viewer
to read the text and see the person speaking.

Generally, vertical displacement should be used to avoid obscuring important information (such as captions) while horizontal displacement should be reserved for indicating speakers (see
[Identifying Speakers](#Identifying-speakers)).

<figure>
<img src="/accessibility/forproducts/guides/subtitles/img/quiz-text-position-1.png" alt="Image showing subtitles placed vertically so that they obscure important onscreen text, which in this case are contestant's names on a quiz show.">
<figcaption class="diagram-annotation">
<i class="diagram-icon icon-bad"></i>
<p>This is bad, placing subtitles here would cover the names.</p>
</figcaption>
</figure>
<figure>
<img src="/accessibility/forproducts/guides/subtitles/img/quiz-text-position-2.png" alt="Image showing the same quiz image, with subtitles moved up to avoid the faces and the onscreen text, which can now be read.">
<figcaption class="diagram-annotation">
<i class="diagram-icon icon-good"></i>
<p>This is better, in this instance, the subtitles should go here so that the names can be read.</p>
</figcaption>
</figure>

In some cases vertical displacement is not sufficient to avoid obscuring important information,
for example when placing the captions above a graphic would cover a face.
In such cases,
[horizontal positioning](#Horizontal-positioning) may be used.

<aside aria-description="Developer information">
Vertical positioning is controlled mainly by the
region element, which is defined using
extent and origin.
However, other attributes can also affect positioning within the region. See display alignment for more details.
</aside>

#### 10.2 Under image positioning {#Under-image-positioning}

Some platforms (e.g. online media player) support the display of subtitles under the image. If the media player is embedded in the page the layout should change to accommodate the subtitle display.

When subtitles are displayed under the image area, vertical displacement will be ignored by the device and only horizontal positioning will be used (e.g. to identify speakers).

#### 10.3 Horizontal positioning {#Horizontal-positioning}

Prepared subtitles are normally centre-aligned within a subtitle region that is horizontally centred relative to the video. Live subtitles (cued blocks and cumulative) are normally left-aligned.

Other horizontal positioning may be used to:
- Avoid obscuring important information (such as captions and mouths) when [vertical positioning](#Vertical-positioning) is not sufficient (see below).
- Indicate the direction of off-screen sounds. See [arrows for off-screen voices](#Use-arrows-for-off-screen-voices).
- Identifying in-vision speakers (legacy technique). See [Identifying speakers with horizontal positioning.](#Use-horizontal-positioning)

In some cases [vertical
positioning](#Vertical-positioning) is not sufficient to avoid obscuring important information, for example when placing the captions above a graphic would cover a face. In such cases, prioritise the important information over speaker identification, using horizontal positioning
if appropriate.

<figure>
<img src="/accessibility/forproducts/guides/subtitles/img/11.1-1-1.png" alt="Image showing subtitle positioned vertically to avoid obscuring text in the bottom right of the image, resulting in it obscuring the mouth of the person speaking.">
<figcaption class="diagram-annotation">
<i class="diagram-icon icon-bad"></i>
<p>This is bad, placing the subtitles here would obscure the speaker's mouth.</p>
</figcaption>
</figure>
<figure>
<img src="/accessibility/forproducts/guides/subtitles/img/11.1-1-2.png" alt="Image showing subtitle moved horizontally instead of vertically to avoid obscuring a face, as happened in the previous image.">

<figcaption class="diagram-annotation">
<i class="diagram-icon icon-good"></i>
<p>This is better, prioritise the graphic over the speaker's identification, or longer and fewer lines.</p>
</figcaption>
</figure>

<aside aria-description="Developer information">
Horizontal positioning is controlled by the
region element, whose size and position are defined using extent and origin. Within the region, horizontal alignment of lines is achieved using
text alignment and multi-row alignment.
</aside>

### 11 Intonation and emotion {#Intonation-and-emotion}

#### 11.1 Sarcasm {#Sarcasm}

To indicate a sarcastic statement, use an exclamation mark in brackets (without a space in between):

<samp class="example">Charming(!)</samp>

To indicate a sarcastic question, use a question mark in brackets:

<samp class="example">You're not going to
work today, are you(?)</samp>

#### 11.2 Stress {#Stress}

Use caps to indicate when a word is stressed. Do not overuse this device - text sprinkled with caps can be hard to read. However, do not underestimate how useful the occasional indication of stress can be for conveying meaning:

<samp class="example">It's the BOOK I want,
not the paper.</samp>

<samp class="example">I know that, but WHEN
will you be finished?</samp>

The word "I" is a special case. If you have to emphasise it in a sentence, make it a different colour from the surrounding text. However, this is rare and should be used sparingly and only when there is no other way to emphasise the word.

<samp class="example"><span style="color:cyan;">She knows. Elaine wrote to her.</span> But<br>if <span style="color:yellow;">I</span> write, she'll know it's urgent.</samp>

Use caps also to indicate when words are shouted or screamed:

<samp class="example">HELP ME!</samp>

However, avoid large chunks of text in caps as they can be hard to read.

##### 11.2.1 Italics {#Italics}

<u class="flag-online">online</u> Subtitles for online exclusives can use italics for emphasis instead of caps (this is an experimental option and should not be included for general use). If this approach is adopted italics should be
used in most instances, with caps reserved for heavier emphasis (e.g. shouting).

Note that there is currently little research to indicate the effectiveness of italics for emphasis in subtitles.

<aside aria-description="Developer information">
Italics can be specified by using `tts:fontStyle="italic"` on a style [referenced](#Element-references-and-xml-id-attributes) by a span.
</aside>

#### 11.3 Whisper {#Whisper}

To indicate whispered speech, a label is most effective.

<samp class="example">WHISPERS:<br>
Don't let him near you.</samp>

However, when time is short, place brackets around the whispered speech:

<samp class="example">(Don't let him near
you.)</samp>

If the whispered speech continues over more than one subtitle, brackets can start to look very messy, so a label in the first subtitle is preferable.

Brackets can also be used to indicate an aside, which may or may not be whispered.

#### 11.4 Incredulous question {#Incredulous-question}

Indicate questions asked in an incredulous tone by means of a question mark followed by an exclamation mark (no space):

<samp class="example">You mean you're going
to marry him?!</samp>

### 12 Accents {#Accents}

This section deals with accents in speech and dialects. For accented characters see [Typography](#Typography).

#### 12.1 Indicate accent only when required {#Indicate-accent-only-when-required}

Do not indicate accent as a matter of course, but only where it is relevant for the viewer's understanding. This is rarely the case in serious/straight news reports, but may well be relevant in lighter factual items. For example, you would
only indicate the nationality of a foreign scientist being interviewed on Horizon or the Ten O’Clock News if it were relevant to the subject matter and the viewer could not pick the information up from any other source, e.g. from their
actual words or any accompanying graphics. However, in a drama or comedy where a character's accent is crucial to the plot or enjoyment, the subtitles must establish the accent when we first see the character and continue to reflect it
from then on.

#### 12.2 Indicate accent sparingly {#Indicate-accent-sparingly}

When it is necessary to indicate accent, bear in mind that, although the subtitler's aim should always be to reproduce the soundtrack as faithfully as possible, a phonetic representation of a speaker's foreign or regional accent or dialect
is likely to slow up the reading process and may ridicule the speaker. Aim to give the viewer a flavour of the accent or dialect by spelling a few words phonetically and by including any unusual vocabulary or sentence construction that
can be easily read. For a Cockney speaker, for instance, it would be appropriate to include quite a few "caffs", "missus" and "ain'ts", but not to replace every single dropped "h" and "g" with an apostrophe.

#### 12.3 Incorrect grammar {#Incorrect-grammar}

You should not correct any incorrect grammar that forms an essential part of dialect, e.g. the Cockney "you was".

A foreign speaker may make grammatical mistakes that do not render the sense incomprehensible but make the subtitle difficult to read in the given time. In this case, you should either give the subtitle more time or change the text as necessary:

<samp class="example">I and my wife is
being marrying four years since and are having four childs,
yes</samp>

This could be changed to:

<samp class="example">I and my wife have
been married four years and have four childs, yes</samp>

#### 12.4 Use label {#Use-label}

The speech text alone may not always be enough to establish the origin of an overseas/regional speaker. In that case, and if it is necessary for the viewer's understanding of the context of the content, use a label to make the accent clear:

<samp class="example">AMERICAN ACCENT:<br>
All the evidence points to a plot.</samp>

### 13 Difficult speech {#Difficult-speech}

#### 13.1 Edit lightly {#Edit-lightly}

Remember that what might make sense when it is heard might make little or no sense when it is read. So, if you think the viewer will have difficulty following the text, you should make it read clearly. This does not mean that you should always
sub-edit incoherent speech into beautiful prose. You should aim to tamper with the original as little as possible - just give it the odd tweak to make it intelligible. (Also see [Accents](#Accents))

#### 13.2 Consider the dramatic effect {#Consider-the-dramatic-effect}

The above is more applicable to factual content, e.g. News and documentaries. Do not tidy up incoherent speech in drama when the incoherence is the desired effect.

#### 13.3 Use labels for incoherent speech {#Use-labels-for-incoherent-speech}

If a piece of speech is impossible to make out, you will have to put up a label saying why:

<samp class="example">(SLURRED): But I love
you!</samp>

Avoid subjective labels such as "UNINTELLIGIBLE" or "INCOMPREHENSIBLE" or "HE BABBLES INCOHERENTLY".

#### 13.4 Use labels for inaudible speech {#Use-labels-for-inaudible-speech}

Speech can be inaudible for different reasons. The subtitler should put up a label explaining the cause.

<samp class="example">APPLAUSE DROWNS
SPEECH</samp>

<samp class="example">TRAIN DROWNS HIS
WORDS</samp>

<samp class="example">MUSIC DROWNS
SPEECH</samp>

<samp class="example">HE MOUTHS</samp>

#### 13.5 Explain pauses in speech {#Explain-pauses-in-speech}

Long speechless pauses can sometimes lead the viewer to wonder whether the subtitles have failed. It can help in such cases to insert explanatory text such as:

<samp class="example">INTRODUCTORY
MUSIC</samp>

<samp class="example">LONG PAUSE</samp>

<samp class="example">ROMANTIC
MUSIC</samp>

#### 13.6 Break up subtitles slow speech {#Break-up-subtitles-slow-speech}

If a speaker speaks very slowly or falteringly, break your subtitles more often to avoid having slow subtitles on the screen. However, do not break a sentence up so much that it becomes difficult to follow.

#### 13.7 Indicate stammer {#Indicate-stammer}

If a speaker stammers, give some indication (but not too much) by using hyphens between repeated sounds. This is more likely to be needed in drama than factual content. Letters to show a stammer should follow the case of the first letter of
the word.

<samp class="example">I'm g-g-going
home</samp>

<samp class="example">W-W-What are you
doing?</samp>

### 14 Hesitation and interruption {#Hesitation-and-interruption}

#### 14.1 Indicate hesitation only if important {#Indicate-hesitation-only-if-important}

If a speaker hesitates, do not edit out the "ums" and "ers" if they are important for characterisation or plot. However, if the hesitation is merely incidental and the "ums" actually slow up the reading process, then edit them out. (This is
most likely to be the case in factual content, and too many "ums" can make the speaker appear ridiculous.)

#### 14.2 Within a single subtitle {#Within-a-single-subtitle}

When the hesitation or interruption is to be shown within a single subtitle, follow these rules:

##### 14.2.1 Pause within a sentence {#Pause-within-a-sentence}

To indicate a pause within a sentence, insert three dots at the point of pausing, then continue the sentence immediately after the dots, without leaving a space.

<samp class="example">Everything that
matters...is a mystery</samp>

You may need to show a pause between two sentences within one subtitle. For example, where a phone call is taking place and we can only witness one side of it, there may not be time to split the sentences into separate subtitles to show that
someone we can't see or hear is responding. In this case, you should put two dots immediately before the second sentence.

<samp class="example">How are you? ..Oh,
I'm glad to hear that.</samp>

A very effective technique is to use [cumulative subtitles](#Cumulative-subtitles), where the first part appears before the second, and both remain on screen until the next subtitle. Use this method only when the content justifies
it; standard prepared subtitles should be displayed in blocks.

##### 14.2.2 Unfinished sentence {#Unfinished-sentence}

If the speaker simply trails off without completing a sentence, put three dots at the end of their speech. If they then start a new sentence, no continuation dots are necessary.

<samp class="example">Hello, Mr... Oh,
sorry! I've forgotten your name</samp>

##### 14.2.3 Unfinished question/exclamation {#Unfinished-question-exclamation}

If the unfinished sentence is a question or exclamation, put three dots (not two) before the question mark or exclamation mark.

<samp class="example">What do you think you're...?!</samp>

##### 14.2.4 Interruption {#Interruption}

If a speaker is interrupted by another speaker or event, put three dots at the end of the incomplete speech.

#### 14.3 Across subtitles {#Across-subtitles}

When the hesitation or interruption occurs in the middle of a sentence that is split across two subtitles, do the following:

##### 14.3.1 Indicate time lapse with dots {#Indicate-time-lapse-with-dots}

Where there is no time-lapse between the two subtitles, put three dots at the end of the first subtitle but no dots in the second one.

<samp class="example">I think...<br>
I would like to leave now.</samp>

Where there is a time-lapse between the two subtitles, put three dots at the end of the first subtitle and two dots at the beginning of the second, so that it is clear that it is a continuation.

<samp class="example">I'd like...</samp>

<samp class="example">..a piece of
chocolate cake</samp>

Remember that dots are only used to indicate a pause or an unfinished sentence. You do not need to use dots every time you split a sentence across two or more subtitles.

### 15 Humour {#Humour}

In humorous sequences, it is important to retain as much of the humour as possible. This will affect the editing process as well as when to leave the screen clear.

#### 15.1 Separate punchlines {#Separate-punchlines}

Try wherever possible to keep punchlines separate from the preceding text.

#### 15.2 Reactions {#Reactions}

Where possible, allow viewers to see actions and facial expressions which are part of the humour by leaving the screen clear or by editing. Try not to leave a subtitle on screen when the next shot contains no speech and shows the character's
reaction, as this distracts from the reaction and spoils the punchline.

#### 15.3 Keep catchphrases {#Keep-catchphrases}

Never edit characters' catchphrases.

### 16 Music and songs {#Music-and-songs}

<aside aria-description="Developer information">
 documents should set music role on the relevant paragraph or span element to indicate that the contents represent music.
</aside>

#### 16.1 Label source music {#Label-source-music}

All music that is part of the action, or significant to the plot, must be indicated in some way. If it is part of the action, e.g. somebody playing an instrument/a record playing/music on a jukebox or radio, then write the label in upper case:

<samp class="example">SHE WHISTLES A JOLLY
TUNE</samp>

<samp class="example">POP MUSIC ON
RADIO</samp>

<samp class="example">MILITARY BAND PLAYS
SWEDISH NATIONAL ANTHEM</samp>

#### 16.2 Describe incidental music {#Describe-incidental-music}

If the music is "incidental music" (i.e. not part of the action) and well known or identifiable in some way, the label begins "MUSIC:" followed by the name of the music (music titles should be fully researched). "MUSIC" is in caps (to indicate
a label), but the words following it are in upper and lower case, as these labels are often fairly long and a large amount of text in upper case is hard to read.

<samp class="example">MUSIC: "The Dance Of
The Sugar Plum Fairy"<br>
by Tchaikovsky</samp>

<samp class="example">MUSIC: "God Save The
Queen"</samp>

<samp class="example">MUSIC: A waltz by
Victor Herbert</samp>

<samp class="example">MUSIC: The Swedish
National Anthem</samp>

(The Swedish National Anthem does not have quotation marks around it as it is not the official title of the music.)

#### 16.3 Combine source and incidental music {#Combine-source-and-incidental-music}

Sometimes a combination of these two styles will be appropriate:

<samp class="example">HE HUMS "God Save The
Queen"</samp>

<samp class="example">SHE WHISTLES "The
Dance Of The Sugar Plum Fairy"<br>
by Tchaikovsky</samp>

#### 16.4 Label mood music only when required {#Label-mood-music-only-when-required}

If the music is "incidental music" but is an unknown piece, written purely to add atmosphere or dramatic effect, do not label it. However, if the music is not part of the action but is crucial for the viewer’s understanding of the plot, a
sound-effect label should be used:

<samp class="example">EERIE
MUSIC</samp>

#### 16.5 Indicate song lyrics with # {#Indicate-song-lyrics-with}

Song lyrics are almost always subtitled - whether they are part of the action or not. Every song subtitle starts with a white hash mark (#) and the final song subtitle has a hash mark at the start and the end:

<samp class="example"># These foolish
things remind me of you #</samp>

There are two exceptions:
- In cases where you consider the visual information on the screen to be more important than the song lyrics, leave the screen free of subtitles.
- Where snippets of a song are interspersed with any kind of speech, and it would be confusing to subtitle both the lyrics and the speech, it is better to put up a music label and to leave the lyrics unsubtitled.

<u class="flag-online">online</u> Instead of # the symbol, ♫ may be used.

#### 16.6 Avoid editing lyrics {#Avoid-editing-lyrics}

Song lyrics should generally be verbatim, particularly in the case of well-known songs (such as God Save The Queen), which should never be edited. This means that the timing of song lyric subtitles will not always follow the conventional timings
for speech subtitles, and the subtitles may sometimes be considerably faster.

If, however, you are subtitling an unknown song, specially written for the content and containing lyrics that are essential to the plot or humour of the piece, there are a number of options:
- edit the lyrics to give viewers more time to read them
- combine song-lines wherever possible
- do a mixture of both - edit and combine song-lines.

NB: If you do have to edit, make sure that you leave any rhymes intact.

#### 16.7 Synchronise with audio {#Synchronise-with-audio}

Song lyric subtitles should be kept closely in sync with the soundtrack. For instance, if it takes 15 seconds to sing one line of a hymn, your subtitle should be on the screen for 15 seconds.

Song subtitles should also reflect as closely as possible the rhythm and pace of a performance, particularly when this is the focus of the editorial proposition. This will mean that the subtitles could be much faster or slower than the conventional
timings.

There will be times where the focus of the content will be on the lyrics of the song rather than on its rhythm - for example, a humorous song like Ernie by Benny Hill. In such cases, give the reader time to read the lyrics by combining song-lines
wherever possible. If the song is unknown, you could also edit the lyrics, but famous songs like Ernie must not be edited.

Where shots are not timed to song-lines, you should either take the subtitle to the end of the shot (if it's only a few frames away) or end the subtitle before the end of the shot (if it's 12 frames or more away).

#### 16.8 Centre lyrics subtitles {#Centre-lyrics-subtitles}

All song-lines should be centred on the screen.

<aside aria-description="Developer information">
This can be achieved by [referencing](#Element-references-and-xml-id-attributes) a region that is positioned centrally (horizontally), and a style with
center alignment and multi-row alignment
either unspecified or set to `"auto"`.
</aside>

#### 16.9 Punctuation {#Punctuation}

It is generally simpler to keep punctuation in songs to a minimum, with punctuation only within lines (when it is grammatically necessary) and not at the end of lines (except for question marks). You should, though, avoid full stops in the
middle of otherwise unpunctuated lines. For example,

<samp class="example">Turn to wisdom.
Turn to joy<br>
There’s no wisdom to destroy</samp>

Could be changed to:

<samp class="example"># Turn to wisdom,
turn to joy<br>
There’s no wisdom to destroy</samp>

In formal songs, however, e.g. opera and hymns, where it could be easier to determine the correct punctuation, it is more appropriate to punctuate throughout.

The last song subtitle should end with a full stop, unless the song continues in the background.

If the subtitles for a song don't start from its first line, show this by using two continuation dots at the beginning:

<samp class="example"># ..Now I need a
place to hide away<br>

# Oh, I believe in yesterday. #</samp>

Similarly, if the song subtitles do not finish at the end of the song, put three dots at the end of the line to show that the song continues in the background or is interrupted:

<samp class="example"># I hear words I
never heard in the Bible... #</samp>

### 17 Sound effects {#Sound-effects}

<aside aria-description="Developer information">
 Sound effects should be labelled as such using an appropriate appropriate role metadata, for example by adding the attribute sound role to the paragraph element.
</aside>

#### 17.1 Subtitle effects only when necessary {#Subtitle-effects-only-when-necessary}

As well as dialogue, all editorially significant sound effects must be subtitled. This does not mean that every single creak and gurgle must be covered - only those which are crucial for the viewer's understanding of the events on screen,
or which may be needed to convey flavour or atmosphere, or enable them to progress in gameplay, as well as those which are not obvious from the action. A dog barking in one scene could be entirely trivial; in another it could be a vital
clue to the story-line. Similarly, if a man is clearly sobbing or laughing, or if an audience is clearly clapping, do not label.

Do not put up a sound-effect label for something that can be subtitled. For instance, if you can hear what John is saying, JOHN SHOUTS ORDERS would not be necessary.

#### 17.2 Describe sounds, not actions {#Describe-sounds--not-actions}

Sound-effect labels are not stage directions. They describe sounds, not actions:

<samp class="example">GUNFIRE</samp>

not:

<samp class="example"><s>THEY SHOOT EACH OTHER</s></samp>

#### 17.3 Format {#Format}

A sound effect should be typed in white caps. It should sit on a separate line and be placed to the left of the screen - unless the sound source is obviously to the right, in which case place to the right.

<aside aria-description="Developer information">
There is no style attribute that enforces all caps; the text needs to be capitalised within the subtitle document.
</aside>

#### 17.4 Subject + verb {#Subject---verb}

Sound-effect labels should be as brief as possible and should have the following structure: subject + active, finite verb:

<samp class="example">FLOORBOARDS
CREAK</samp>

<samp class="example">JOHN SHOUTS
ORDERS</samp>

Not:

<samp class="example"><s>CREAKING OF FLOORBOARDS</s></samp>

Or

<samp class="example"><s>FLOORBOARDS CREAKING</s></samp>

Or

<samp class="example"><s>ORDERS ARE SHOUTED BY JOHN</s></samp>

<aside aria-description="Developer information">
There is no obvious value for `ttm:role` for such labels. The closest fit is probably `"description"`.
</aside>

#### 17.5 In-vision translations {#In-vision-translations}

If a speaker speaks in a foreign language and in-vision translation subtitles are given, use a label to indicate the language that is being spoken. This should be in white caps, ranged left above the in-vision subtitle, followed by a colon.
Time the label to coincide with the timing of the first one or two in-vision subtitles. Bring it in and out with shot-changes if appropriate.

<img src="/accessibility/forproducts/guides/subtitles/img/Tokyo.jpeg" alt="Screen shot of Japanese temple with subtitle IN JAPANESE: above burnt-in translation" title="Photo by Nigel Megitt" style="width:100%;">

If there are a lot of in-vision subtitles, all in the same language, you only need one label at the beginning - not every time the language is spoken.

If the language spoken is difficult to identify, you can use a label saying TRANSLATION:, but only if it is not important to know which language is being spoken. If it is important to know the language, and you think the hearing viewer would
be able to detect a language change, then you must find an appropriate label.

#### 17.6 Animal noises {#Animal-noises}

The way in which subtitlers convey animal noises depends on the content style. In factual wildlife, for instance, lions would be labelled:

<samp class="example">LIONS ROAR</samp>

However, in an animation or a game, it may be more appropriate to convey animal noises phonetically. For instance, "LIONS ROAR" would become something like:

<samp class="example">Rrrarrgghhh!</samp>

### 18 Numbers {#Numbers}

#### 18.1 Spelling out {#Spelling-out}

In general, the numeral form should be used. However, you can spell out numbers when this is editorially justified as detailed below.

The numbers 1-10 are often better spelled out:

<samp class="example">I'll see you in three days</samp>

<samp class="example"><s>I'll see you in 3 days</s></samp>

But use the numeral with units:

<samp class="example">It takes 1kJ of energy to lift
someone.</samp>

<samp class="example"><s>It
takes one kJ of energy to lift someone.</s></samp>

Emphatic numbers are always spelled out:

<samp class="example">She gave me hundreds of reasons</samp>

<samp class="example"><s>She
gave me 100s of reasons</s></samp>

Spell out any number that begins a sentence:

<samp class="example">Three days from now.</samp>

<samp class="example"><s>3
days from now.</s></samp>

If there is more than one number in a sentence or list, it may be more appropriate to display them as numerals instead of words:

<samp class="example">On her 21st birthday party, 54 guests
turned up</samp>

Consistency is important, so avoid

<samp class="example"><s>the
score was three - 1</s></samp>

Numerals over 4 digits must include appropriately placed commas:

<samp class="example">There are 1,500 cats here.</samp>

For sports, competitions, games or quizzes, always use numerals to display points, scores or timings.

#### 18.2 Dates {#Dates}

For displaying the day of the month, use the appropriate numeral followed by lowercase "th", "st" or "nd":

<samp class="example">April 2nd.</samp>

#### 18.3 Money {#Money}

##### 18.3.1 Sterling {#Sterling}

Use the numerals plus the £ sign for all monetary amounts except where the amount is less than £1.00:

<samp class="example">We paid £50.</samp>

For amounts less than £1.00 the word "pence" should be used after the numeral:

<samp class="example">58 pence.</samp>

If the word "pound" is used in sentence without referring to a specific amount, then the word must be used, not the symbol.

##### 18.3.2 Other currencies {#Other-currencies}

See the [list of supported characters](#Supported-characters) for currency symbols you can use for broadcast and online.

<u class="flag-broadcast">broadcast</u> Spell out other currencies, including Euro (the Euro symbol is not supported in Teletext).

<u class="flag-online">online</u> Use the correct Unicode symbol for the currency, e.g. the Euro symbol €.

<aside aria-description="Developer information">
All subtitle documents should be encoded in UTF-8,
however the actual set of code points usable in an
 document intended for broadcast presentation is currently restricted to the .
 No such restriction exists for documents intended for online-only presentation, however care should be taken that there is a reasonable expectation that the presentation device will have a font
installed that contains glyphs for all the code points used.
</aside>

#### 18.4 Time {#Time}

Indicate the time of the day using numerals in a manner which reflects the spoken language:

<samp class="example">The time now is

4:30</samp>

<samp class="example">The alarm went off at
4 o’clock</samp>

#### 18.5 Measurement {#Measurement}

Never use symbols for units of measurement.

Abbreviations can be used to fit text in a line, but if the unit of measurement is the subject do not abbreviate.

### 19 Cumulative subtitles {#Cumulative-subtitles}

A cumulative subtitle consists of two or three parts - usually complete sentences. Each part will appear on screen at a different time, in sync with its speaker, but all parts will have an identical out-cue.

#### 19.1 Use only when necessary {#Use-only-when-necessary}

Cumulatives should only be used when there is a good reason to delay part of the subtitle (e.g. dramatic impact/song rhythm) and no other way of doing it - i.e. there is insufficient time available to split the subtitle completely.

This is most likely to happen in an interchange between speakers, where the first speaker talks much faster than the second. Delaying the speech of the second person by using a cumulative means that the first subtitle will still be on screen
long enough to be read, while at the same time the speech is kept in sync.

#### 19.2 Common scenarios {#Common-scenarios}

Cumulatives are particularly useful in the following situations:
- For jokes - to keep punch lines separate
- In quizzes - to separate questions and answers
- In songs - e.g. for backing singers. They are particularly effective when one line starts before the previous one finishes
- To [delay dramatic
responses](#Pause-within-a-sentence) (However, if a response is not expected, a cumulative can give the game away)
- When an exclamation/sound effect label occurs just before a shot-change, and would otherwise need to be merged with the preceding subtitle
- To distinguish between two or more white speakers in the same shot

#### 19.3 Timing {#Timing-2}

Make sure there is sufficient time to read each segment of a cumulative, especially the final one. Consider leaving the final part on screen for a slightly longer time to allow the viewer to scan the line again.

If you use cumulatives in children’s content, observe children’s timings.

<aside aria-description="Developer information">
Further detail on how to specify cumulatives is described in
paragraph and span. Where possible, each individual word that forms part of a cumulative subtitle should be included in the subtitle document exactly once, with appropriate timing specified
by putting groups of words that appear with the same timing within a span with `begin` and `end` attributes. This allows the plain text of the subtitle transcript to be extracted more easily since there is no need to de-duplicate words.
There is an alternative approach in which multiple paragraph elements are each timed to follow on from each other, with the first words being a repeat of the words in the previous paragraph and additional words appended. This approach creates the same
visual effect but should be avoided.
</aside>

#### 19.4 Avoid cumulative where shots change {#Avoid-cumulative-where-shots-change}

Be wary of timing the appearance of the second/third line of a cumulative to coincide with a shot-change, as this may cause the viewer to reread the first line.

#### 19.5 Avoid obscuring important information {#Avoid-obscuring-important-information}

Remember that using a cumulative will often mean that more of the picture is covered. Don’t use cumulatives if they will cover mouths, or other important visuals

#### 19.6 Stick to three lines {#Stick-to-three-lines}

Stick to a maximum of three lines unless you are subtitling a fast quiz like University Challenge where it is preferable to show the whole question in one subtitle and where you will not be obscuring any interesting visuals

### 20 Children’s subtitling {#Children-s-subtitling}

The following guidelines are recommended for the subtitling of programmes targeted at children below the age of 11 years (ITC).

#### 20.1 Editing {#Editing}

There should be a match between the voice and subtitles as far as possible.

A strategy should be developed where words are omitted rather than changed to reduce the length of sentences.

For example,

Can you think why they do this?

<samp class="example">Why do they do
this?</samp>

Can you think of anything you could do with all the heat produced in the incinerator?

<samp class="example">What could you do
with the heat from the incinerator?</samp>

Difficult words should also be omitted rather than changed. For example:

First thing we're going to do is make his big, ugly, bad-tempered head.

<samp class="example">First we're going to
make his big, ugly head.</samp>

All she had was her beloved rat collection.

<samp class="example">She only had her
beloved rat collection.</samp>

Where possible the grammatical structure should be simplified while maintaining the word order.

You can see how metal is recycled if we follow the aluminium.

<samp class="example">See how metal is
recycled by following the aluminium.</samp>

We need energy so our bodies can grow and stay warm.

<samp class="example">We need energy to
grow and stay warm.</samp>

Difficult and complex words in an unfamiliar context should remain on screen for as long as possible. Few other words should be used. For example:

Nurse, we'll test the reflexes again.

<samp class="example">Nurse, we'll test the
reflexes.</samp>

Air is displaced as water is poured into the bottle.

<samp class="example">The water in the
bottle displaces the air.</samp>

Care should be taken that simplifying does not change the meaning, particularly when meaning is conveyed by the intonation of words.

Often, the aim of schools programmes is to introduce new vocabulary and to familiarize pupils with complex terminology. When subtitling schools programmes, introduce complex vocabulary in very simple sentences and keep it on screen for as
long as possible.

#### 20.2 Preferred timing {#Preferred-timing}

In general, subtitles for children should follow the speed of speech. However, there may be occasions when matching the speed of speech will lead to subtitle rate that is not appropriate for the age group. The producer/assistant producer should
seek advice on the appropriate subtitle timing for a programme.

#### 20.3 Avoid variable timing {#Avoid-variable-timing}

There will be occasions when you will feel the need to go faster or slower than the standard timings - the same guidelines apply here as with adult timings (see [Timing](#Timing)). You should however avoid inconsistent timings e.g.
a two-line subtitle of 6 seconds immediately followed by a two-line subtitle of 8 seconds, assuming equivalent scores for visual context and complexity of subject matter.

#### 20.4 Allow more time for visuals {#Allow-more-time-for-visuals}

More time should be given when there are visuals that are important for following the plot, or when there is particularly difficult language.

#### 20.5 Syntax and Vocabulary {#Syntax-and-Vocabulary}

Do not simplify sentences, unless the sentence construction is very difficult or sloppy.

Avoid splitting sentences across subtitles. Unless this is unavoidable, keep to complete clauses.

Vocabulary should not be simplified.

There should be no extra spaces inserted before punctuation.

### 21 Live subtitling (BBC-ASP, OFCOM-IQLS, OFCOM-GSS) {#Live-subtitling--BBC-ASP--OFCOM-IQLS--OFCOM-GSS}

#### 21.1 General {#General}

The subtitler should have a direct pre-broadcast-encoding feed from the broadcaster, so they can hear the output a few seconds earlier than if relying on the broadcast­ service.

Maintain a regular subtitle output with no long gaps (unless it is obvious from the picture that there is no commentary) even if this means subtitling the picture or providing background information rather than subtitling the commentary.

Aim for continuity in subtitles by following through a train of thought where possible, rather than sampling the commentary at intervals.

Do not subtitle over existing video captions where avoidable (in news, this is often unavoidable, in which case a speaker's name can be included in the subtitle if available).

#### 21.2 Preparation {#Preparation}

Find out specialist vocabulary, and specific editorial guidelines for the genre (e.g. sport). Familiarise yourself with Prepared segments that have been subtitled and their place in the running order, but be prepared for the order to change.

When available to the subtitler, pre-recorded segments should be subtitled prior to broadcast (not live) and cued out at the appropriate moment.

When cueing prepared texts for scripted parts of the programme:
- Try to cue the texts of pre-recorded segments so that they closely match the spoken words in terms of start time.
- Do not cue texts out rapidly to catch up if you get left behind - skip some and continue from the correct place.
- Try to include speakers' names if available where in-vision captions have been obliterated.

#### 21.3 Editing {#Editing-2}

Subtitles should use upper and lower case as appropriate.

Standard spelling and punctuation should be used at all times, even on the fastest programmes.

Produce complete sentences even for short comments because this makes the result look less staccato and hurried.

Strong or inappropriate language must not appear on screen in error.

For news programmes, current affairs programmes and most other genres, subtitles should be verbatim, up to a subtitling speed of around 160-180wpm. Above that speed, some editing would be expected.

For some genres, such as in-play sporting action, the subtitling may be edited more heavily so as to convey vital commentary information while allowing better access to the visuals. (BBC-SPG)

#### 21.4 Corrections {#Corrections}

Any serious or misleading errors in real-time subtitling should be corrected clearly and promptly. The correction should be preceded by two dashes:

<samp class="example">The minster’s shrew
is unchanged -- view.</samp>

However be aware that too many on-air corrections, or corrections that are not sufficiently prompt, can actually make the subtitles harder for a viewer to follow.

Ultimately the subtitler may have to decide whether to make a correction or omit some speech in order to catch up. Sometimes this can be done without detracting from the integrity of the subtitling, but this is not always the case. Do not
correct minor errors where the reader can reasonably be expected to deduce the intended meaning (e.g. typos and misspellings).

If necessary, an apology should be made at the end of the programme. If possible, repeat the subtitle with the error corrected.

#### 21.5 Formatting {#Formatting}

Live subtitles should appear word by word, from left to right, to allow maximum reading time. Live subtitles are justified left (not centred).

<aside aria-description="Developer information">
Live subtitles should be placed in an appropriately sized
region with a preset origin x coordinate (for left to right text; for right to left text ensure the right edge is preset).
A style with text alignment set to `"start"` (always works) or `"left"` for left to right text only or `"right"` for right to left text only should be used.
multi-row alignment should be avoided (i.e. left unset, or set to `"auto"`) since it can result in lines being moved horizontally whenever a new word appears.
</aside>

Two-lines of scrolling text should be used.

For live subtitling, use a reduced set of formatting techniques. Focus on colour and vertical positioning.
- A change of speaker should always be indicated by a change of colour.
- Scrolling subtitles, while usually appearing at the bottom of the screen, should be raised as appropriate in order to avoid any vital action, visual information, name labels, etc.

<aside aria-description="Developer information">
Subtitle vertical position can be set by [referencing](#Element-references-and-xml-id-attributes) a region with appropriate origin, extent and display alignment attributes.
An alternative strategy is to insert line break elements as necessary; for example if `tts:displayAlign="after"` then every line break element appended after a subtitle will raise that subtitle by the height of the line. Although
using line breaks for positioning is discouraged for prepared subtitles (see [Authoring font size](#Authoring-font-size)), this technique saves time when live subtitling. Note that if the region height is exceeded by entering too many
line breaks, lines can 'fall off' the top, and be clipped.
If a subtitle needs to be moved while it is visible and inserting line break elements is not possible then the paragraph should be ended and a new paragraph begun that references a differently positioned region. That new paragraph
can contain the same words and style references.
</aside>

## APPENDICES {#APPENDICES}

### 33 Appendix 6: BBC subtitle workflows {#Appendix-BBC-subtitle-workflows}

<figure>
<figcaption>
This diagram is a high-level view of current subtitle workflows:</figcaption>
[Workflow diagram - see BBC documentation for current subtitle workflows]
</figure>

### 34 Appendix 7: References {#Appendix-References}
- ‘BBC Access Services Presentation & Style Guidelines’ (internal document). 2012
- [‘bbc.co.uk Online Subtitling Editorial
Guidelines V1.1’. 2009. (archived via the Wayback Machine)](https://web.archive.org/web/20120403102830/https://www.bbc.co.uk/guidelines/futuremedia/accessibility/subtitling_guides/online_sub_editorial_guidelines_vs1_1.pdf)
- [BBC
R&D White Paper 287 (PDF): A Survey of UK Television Viewing
Conditions. 2015](https://downloads.bbc.co.uk/rd/pubs/whp/whp-pdf-files/WHP287.pdf)
- [‘Specification of the EBU Subtitling data
exchange format', TECH. 3264-E. 1991](https://tech.ebu.ch/publications/tech3264)
- [‘ITC Guidance on Standards for
Subtitling’. 1999. (Word document download)](https://webarchive.nationalarchives.gov.uk/20100508023348/http://www.ofcom.org.uk/tv/ifi/guidance/tv_access_serv/archive/subtitling_stnds/itc_stnds_subtitling_word.doc)
- ['The quality of live subtitling -
Improving the viewer experience'. 2013, Ofcom.](https://www.ofcom.org.uk/__data/assets/pdf_file/0017/45602/subtitling.pdf)

