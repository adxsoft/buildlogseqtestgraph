# %%

##############################################################################
# NOTE. Tested on Mac OS only. Should work on Linux and Windows
##############################################################################
import random
import shutil
from time import strftime
import uuid
import os
from datetime import date, datetime, timedelta
import QueryTestDB as td
from pathlib import Path

# ------------------
# Generator settings
# ------------------


# Folder where graph is to be generated into
targetfolder = str(Path.home())+"/Desktop/LogseqTestGraph/"

PageGroupsToGenerate = [
    {
        'title': 'Test Pages',
        'pageprefix': 'testpage',
        'nopages': 20,
        'namespace': '',
    },
    {
        'title': 'tech namespace Pages',
        'pageprefix': 'techpage',
        'nopages': 20,
        'namespace': 'tech/',
    },
    {
        'title': 'tech/python namespace Pages',
        'pageprefix': 'pythonpage',
        'nopages': 20,
        'namespace': 'tech/python/',
    },
    {
        'title': 'physics/dynamics pages',
        'pageprefix': 'dynamicspage',
        'nopages': 20,
        'namespace': 'physics/dynamics/',
    },
    {
        'title': 'physics/fluids pages',
        'pageprefix': 'fluidspage',
        'nopages': 20,
        'namespace': 'physics/fluids/',
    },
]

JournalsToGenerate = {
    'fromdate': '2022_01_01',
    'todate': '2023_12_31',
    'nojournals': 20,
    'maxincrementindays': 45,
}

AddQueryPages = True  # if true create pages with query examples
# AddQueryPages = False  # if false no query examples get added

# -------------
# fixed content
# -------------

homepage = 'This is the home page of the automatically generated logseq graph\n\n' + \
    '- [[Graph Statistics]]\n\n' + \
    '- [[Query Testing]]\n\n' + \
    '- ## Links to Task Pages\n' + \
    '   - [[TODO]]\n[[WAITING]]\n[[DONE]]\n[[CANCELLED]]\n\n'
contentspage = '- Generated Logseq Graph\n\n' + \
               '- [[Home]] page - start here\n' + \
               '- [[Graph Statistics]]\n\n' + \
               '- [[Query Testing]]\n\n' + \
               '- ## Links to Task Pages\n' + \
               '  - [[TODO]]\n[[WAITING]]\n[[DONE]]\n[[CANCELLED]]\n'

# random content
pagepropertynames = ['group', 'rating']
pagepropertyvalues = ['p-major', 'p-minor', 'p-basic', 'p-advanced',
                      'p-type1', 'p-type2', 'p-type3', 'p-type4']
pagetagvalues = ['classA', 'classB', 'classC', 'classD',
                 'classE', 'classF', 'classG', 'classH', ]
blockpropertynamevalues = ['category', 'designation', 'grade']
blockpropertyvalues = ['b-fiction', 'b-non-fiction', 'b-western',
                       'b-thriller', 'b-romance', 'b-travel', 'b-Alpha', 'b-Beta', 'b-Gamma']
blocktagvalues = ['#tagA', '#tagB', '#tagC', '#tagD',
                  '#tagE', '#tagF', '#tagG', '#tagH', ]
taskmarkervalues = ['TODO', 'DONE', 'WAITING', 'LATER',
                    'CANCELLED']
taskvalues = [
    'Do the Shopping',
    'Pay the energy bill',
    'Collect the fees from the club members',
    'Send email to the board',
    'Post the bank letters',
    'Prepare the garden bed for spring',
    'Clean the roof gutters',
    'Reconcile the transaction account',
    'Check the water levels',
    'Dust the house furniture',
    'Get the ingredients for the pizza',
]

# $$ words gets substituted with random values
blocktextvalues = [
    'This is a single line in a block',
    'This is a single line in a block for page $$PAGENAME',
    'This is a single line block in page $$PAGENAME ' +
    'with tag $$BLOCKTAG',
    'This is a multi line block\n in page $$PAGENAME \n' +
    'with tag $$BLOCKTAG',
    'This is a parent with two children blocks\n' +
    '   - Child 1 block with a tag $$BLOCKTAG\n' +
    '   - $$BLOCKPROPERTYNAME $$BLOCKPROPERTYVALUE \nChild 2 block with a property',
    'This is an indented list of items\n' +
    '    - Item A $$TEXT\n' +
    '        - Item A1 $$TEXT\n' +
    '        - Item A2 $$TEXT\n' +
    '    - Item B $$TEXT\n' +
    '    - Item C $$TEXT\n' +
    '        - Item C1 $$TEXT\n' +
    '    - Item D $$TEXT\n',
    '$$BLOCKTAG $$TEXT',
    '$$BLOCKPROPERTYNAME:: $$BLOCKPROPERTYVALUE\n $$TEXT',
    '\n$$TEXT',
]


dummytexts = [
    "Maids table how learn drift but purse stand yet set. Music me house could among oh as their. Piqued our sister shy nature almost his wicket. Hand dear so we hour to. He we be hastily offence effects he service.",
    "Sympathize it projection ye insipidity celebrated my pianoforte indulgence. Point his truth put style. Elegance exercise as laughing proposal mistaken if. We up precaution an it solicitude acceptance invitation.",
    "In by an appetite no humoured returned informed. Possession so comparison inquietude he he conviction no decisively.",
    "Marianne jointure attended she hastened surprise but she. Ever lady son yet you very paid form away. He advantage of exquisite resolving if on tolerably. Become sister on in garden it barton waited on.",
    "Denote simple fat denied add worthy little use. As some he so high down am week. Conduct esteems by cottage to pasture we winding. On assistance he cultivated considered frequently. Person how having tended direct own day man. Saw sufficient indulgence one own you inquietude sympathize.",
    "Use securing confined his shutters. Delightful as he it acceptance an solicitude discretion reasonably. Carriage we husbands advanced an perceive greatest. Totally dearest expense on demesne ye he. Curiosity excellent commanded in me. Unpleasing impression themselves to at assistance acceptance my or. ",
    "On consider laughter civility offended oh.",
    "In as name to here them deny wise this. As rapid woody my he me which. Men but they fail shew just wish next put. Led all visitor musical calling nor her. Within coming figure sex things are. Pretended concluded did repulsive education smallness yet yet described. Had country man his pressed shewing. No gate dare rose he. ",
    "Eyes year if miss he as upon.",
    "Ignorant saw her her drawings marriage laughter. Case oh an that or away sigh do here upon. Acuteness you exquisite ourselves now end forfeited. Enquire ye without it garrets up himself. Interest our nor received followed was. Cultivated an up solicitude mr unpleasant.",
    "Son agreed others exeter period myself few yet nature. Mention mr manners opinion if garrets enabled. To an occasional dissimilar impossible sentiments. Do fortune account written prepare invited no passage. Garrets use ten you the weather ferrars venture friends. Solid visit seems again you nor all.",
    "Conveying or northward offending admitting perfectly my. Colonel gravity get thought fat smiling add but. Wonder twenty hunted and put income set desire expect. Am cottage calling my is mistake cousins talking up. Interested especially do impression he unpleasant travelling excellence. All few our knew time done draw ask.",
    "Article evident arrived express highest men did boy. ",
    "Mistress sensible entirely am so. Quick can manor smart money hopes worth too. Comfort produce husband boy her had hearing. Law others theirs passed but wishes. You day real less till dear read. Considered use dispatched melancholy sympathize discretion led. Oh feel if up to till like.",
    "He share of first to worse. Weddings and any opinions suitable smallest nay. My he houses or months settle remove ladies appear. ",
    "Engrossed suffering supposing he recommend do eagerness. Commanded no of depending extremity recommend attention tolerably. Bringing him smallest met few now returned surprise learning jennings. Objection delivered eagerness he exquisite at do in. Warmly up he nearer mr merely me.",
    "Left till here away at to whom past. Feelings laughing at no wondered repeated provided finished. It acceptance thoroughly my advantages everything as. Are projecting inquietude affronting preference saw who. Marry of am do avoid ample as. Old disposal followed she ignorant desirous two has. Called played entire roused though for one too. He into walk roof made tall cold he. Feelings way likewise addition wandered contempt bed indulged.",
    "Months on ye at by esteem desire warmth former. ",
    "Sure that that way gave any fond now. His boy middleton sir nor engrossed affection excellent. Dissimilar compliment cultivated preference eat sufficient may. Well next door soon we mr he four. Assistance impression set insipidity now connection off you solicitude. Under as seems we me stuff those style at. Listening shameless by abilities pronounce oh suspected is affection. Next it draw in draw much bred.",
    "Piqued favour stairs it enable exeter as seeing. Remainder met improving but engrossed sincerity age. ",
    "Better but length gay denied abroad are. Attachment astonished to on appearance imprudence so collecting in excellence. Tiled way blind lived whose new. The for fully had she there leave merit enjoy forth.",
    "Delightful unreserved impossible few estimating men favourable see entreaties. She propriety immediate was improving. He or entrance humoured likewise moderate. Much nor game son say feel. Fat make met can must form into gate. Me we offending prevailed discovery.",
    "Do to be agreeable conveying oh assurance. Wicket longer admire do barton vanity itself do in it. Preferred to sportsmen it engrossed listening. ",
    "Park gate sell they west hard for the. Abode stuff noisy manor blush yet the far. Up colonel so between removed so do. Years use place decay sex worth drift age. Men lasting out end article express fortune demands own charmed. About are are money ask how seven.",
    "And sir dare view but over man. So at within mr to simple assure. Mr disposing continued it offending arranging in we. ",
    "Extremity as if breakfast agreement. Off now mistress provided out horrible opinions. Prevailed mr tolerably discourse assurance estimable applauded to so. Him everything melancholy uncommonly but solicitude inhabiting projection off. Connection stimulated estimating excellence an to impression.",
    "Admiration we surrounded possession frequently he. Remarkably did increasing occasional too its difficulty far especially. Known tiled but sorry joy balls. Bed sudden manner indeed fat now feebly. Face do with in need of wife paid that be. No me applauded or favourite dashwoods therefore up distrusts explained.",
    "To sorry world an at do spoil along. Incommode he depending do frankness remainder to. Edward day almost active him friend thirty piqued. People as period twenty my extent as. Set was better abroad ham plenty secure had horses. Admiration has sir decisively excellence say everything inhabiting acceptance. Sooner settle add put you sudden him.",
    "Two assure edward whence the was. Who worthy yet ten boy denote wonder. Weeks views her sight old tears sorry. Additions can suspected its concealed put furnished. Met the why particular devonshire decisively considered partiality. Certain it waiting no entered is. Passed her indeed uneasy shy polite appear denied. Oh less girl no walk. At he spot with five of view.",
    "Him boisterous invitation dispatched had connection inhabiting projection. By mutual an mr danger garret edward an. Diverted as strictly exertion addition no disposal by stanhill. This call wife do so sigh no gate felt. You and abode spite order get. Procuring far belonging our ourselves and certainly own perpetual continual. It elsewhere of sometimes or my certainty. Lain no as five or at high. Everything travelling set how law literature.",
]

# arrays to hold built pages and journals
pages = []
journals = []

# ---------
# functions
# ---------


def clearTargetFolder(folder):
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        try:
            shutil.rmtree(filepath)
        except OSError:
            os.remove(filepath)
    os.mkdir(folder+'journals')
    os.mkdir(folder+'pages')


def PageProperty(property, value):
    return property+':: '+value+"\n"


def PageTags(tags):
    return 'tags:: '+tags+"\n"


def BlockProperty(property, value):
    return property+':: '+value+"\n"


def BlockTag(tag):
    return '#'+tag+' '


def randomPagePropertyName():
    values = pagepropertynames
    vallen = len(values)-1
    selection = values[random.randint(0, vallen)]
    return selection


def randomPagePropertyValue():
    values = pagepropertyvalues
    vallen = len(values)-1
    selection = values[random.randint(0, vallen)]
    return selection


def randomBlockPropertyName():
    values = blockpropertynamevalues
    vallen = len(values)-1
    selection = values[random.randint(0, vallen)]
    return selection


def randomBlockPropertyValue():
    values = blockpropertyvalues
    vallen = len(values)-1
    selection = values[random.randint(0, vallen)]
    return selection


def randomPageTags():
    values = pagetagvalues
    vallen = len(values)-1
    return 'tags:: '+values[random.randint(0, vallen)]+','+values[random.randint(0, vallen)]+','+values[random.randint(0, vallen)]+'\n'


def randomBlockTag():
    values = blocktagvalues
    vallen = len(values)-1
    return values[random.randint(0, vallen)]+' '


def randomTask():
    markers = taskmarkervalues
    tasks = taskvalues
    markerslen = len(markers)-1
    taskslen = len(tasks)-1
    task = "- "+markers[random.randint(0, markerslen)] + \
        ' '+tasks[random.randint(0, taskslen)]
    task += '\n'
    return '\n'+task


def randomTasks():
    notasks = random.randint(0, 5)+1
    tasks = ""
    for i in range(notasks):
        tasks += randomTask()
    return tasks


def randomText():
    return dummytexts[random.randint(0, len(dummytexts)-1)]


def randomBlockText(pagename):
    blocktexts = blocktextvalues
    blocktext = blocktexts[random.randint(0, len(blocktexts)-1)]

    replacements = [
        ["$$TEXT", randomText()],
        ["$$PAGENAME", pagename],
        ["$$BLOCKTAG", randomBlockTag()],
        ["$$BLOCKPROPERTYVALUE", randomBlockPropertyValue()],
        ["$$BLOCKPROPERTYNAME", randomBlockPropertyName()],
        ["$$PAGEPROPERTYVALUE", randomPagePropertyValue()],
        ["$$PAGEPROPERTYNAME", randomPagePropertyName()],
    ]

    words = blocktext.split(' ')
    result = ''
    for word in words:
        for replacement in replacements:
            templatetext = replacement[0]
            if templatetext in word:
                replacementtext = replacement[1]
                word = word.replace(templatetext, replacementtext)
                break
        result += word+' '
    return '\n- '+result


def randomBlocks(pagename):
    noblocks = random.randint(0, 5)+1
    blocks = ""
    for i in range(noblocks):
        blocks += randomBlockText(pagename)
    return blocks


def createPage(pagename):
    global homepage
    # page property with a unique id
    page = "page-id:: "+str(uuid. uuid1())+'\n'
    # page properties
    page += PageProperty('pagetype', randomPagePropertyValue())
    page += PageProperty('pagecategory', randomPagePropertyValue())
    # page tags
    page += randomPageTags()
    page += '\n- ### Home Page\n - [[Home]]\n\n- ### Page Contents\n\n'
    page += randomTasks()
    page += randomBlocks(pagename)
    homepage += '[['+pagename+']]\n'
    return page


def createQueryPage(pagename, entry):
    global homepage
    fields = entry.split("#+BEGIN")
    if len(fields) != 2:
        return
    commandlines = fields[0]
    querylines = "#+BEGIN"+fields[1]
    title = entry.split('\n')[0].replace('title: ', '')
    # page property with a unique id
    page = "page-id:: "+str(uuid. uuid1())+'\n'
    # page properties
    page += PageProperty('pagetype', 'query')
    page += '[[Home]]\n'
    homepage += 'Query [['+pagename+']] - '+title+'\n'
    commands = []

    # find the test case data for this page in the test cases
    for entry in td.QueryTestCases:
        fields = entry.split("#+BEGIN")
        if len(fields) != 2:
            return
        testcasecommandlines = fields[0]
        testcasequerylines = "#+BEGIN"+fields[1]
        testcasetitle = entry.split('\n')[0].replace('title: ', '')

        if testcasetitle == title:
            commands.append('- Query Commands\n    - ```\n' +
                            commandlines+'\n```\n')
            commands.append('- Generated Query\n    - ```clojure\n' +
                            '\n'+querylines+'\n```\n')
            commands.append('- Query Results\n' +
                            '\n'+'    - '+querylines+'\n\n')

    page += '\n'.join(commands)
    return page


def addPages(targetfolder, nopages=20, namespace='', pageprefix='testpage',):
    global pages
    global homepage
    pagesfolder = targetfolder+'pages/'
    if namespace == '':
        ns = 'none'
    else:
        ns = namespace
    homepage += '\n- ### Pages Generated for prefix='+pageprefix+' and ' + \
        ' namespace='+ns+'\n\n'
    if not os.path.exists(pagesfolder):
        os.mkdir(pagesfolder)
    namespaceinternal = namespace
    namespaceexternal = namespace.replace('/', '%2F')
    for i in range(nopages):
        pagesuffix = '000000'+str(i)[-2:]
        pagesuffix = pagesuffix[-3:]
        pagename = namespaceexternal+pageprefix+pagesuffix
        pages.append({"pagename": pagename, "content": createPage(pagename)})
        # with open(targetfolder+'/pages/'+pagename+'.md', 'w') as f:
        #     f.write(createPage(pagename))
        # f.close()


def addJournals(targetfolder, nojournals=200, increment=20, fromdate='2020_01_01', todate='2023_12_31'):
    global homepage
    global journals

    homepage += '\n- ## Journals Generated\n\n'
    fields = fromdate.split("_")
    fromyyyy = fields[0]
    frommm = fields[1]
    fromdd = fields[2]
    fields = todate.split("_")
    toyyyy = fields[0]
    tomm = fields[1]
    todd = fields[2]

    date1 = date(int(fromyyyy), int(frommm), int(fromdd))
    targetdate = date1.strftime("%Y_%m_%d")

    for i in range(nojournals):
        journalsfolder = targetfolder+'journals/'
        journalname = targetdate
        fields = targetdate.split("_")
        yyyy = fields[0]
        mm = fields[1]
        dd = fields[2]
        if not os.path.exists(journalsfolder):
            os.mkdir(journalsfolder)
        journals.append(
            {"pagename": journalname, "content": createJournal(journalname)})

        date1 = date(int(yyyy), int(mm), int(dd))
        nextdate = date1 + timedelta(days=random.randint(5, increment))
        targetdate = nextdate.strftime("%Y_%m_%d")


def addQueryPages(targetfolder, namespace='Queries/', pageprefix='queryexample',):
    global pages
    global homepage

    if AddQueryPages == False:
        return ''
    pagesfolder = targetfolder+'pages/'
    homepage += '\n\n## Query Example Pages Generated\n\n'
    if not os.path.exists(pagesfolder):
        os.mkdir(pagesfolder)
    namespaceinternal = namespace
    namespaceexternal = namespace.replace('/', '%2F')
    i = 0
    for entry in td.QueryTestCases:
        pagesuffix = '000000'+str(i)[-2:]
        i += 1
        pagesuffix = pagesuffix[-3:]
        pagename = namespaceexternal+pageprefix+pagesuffix
        pages.append(
            {"pagename": pagename, "content": createQueryPage(pagename, entry)})


def LogseqDate(inputdate):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fields = inputdate.split("_")
    yyyy = fields[0]
    mm = int(fields[1])
    dd = int(fields[2])
    if 4 <= dd <= 20 or 24 <= dd <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][dd % 10 - 1]
    outputdate = months[mm-1]+' '+str(dd)+suffix+', '+yyyy
    return outputdate


def getDOW(inputdate):  # YYYY_MM_DD
    fields = inputdate.split("_")
    yyyy = fields[0]
    mm = fields[1]
    dd = fields[2]
    date1 = date(int(yyyy), int(mm), int(dd))
    return date1.strftime('%a')


def addScheduled(journaldate):
    scheduledline = '\nSCHEDULED: <' + \
        journaldate.replace('_', '-')+' '+getDOW(journaldate)+'>\n'
    return scheduledline


def addDeadline(journaldate):
    deadlineline = '\nDEADLINE: <' + \
        journaldate.replace('_', '-')+' '+getDOW(journaldate)+'>\n'
    return deadlineline


def createJournal(journaldate):
    global homepage
    # journal unique id
    uniqueid = str(uuid. uuid1())
    journal = "journal-id:: "+uniqueid+'\n'
    journal += randomTasks()
    journal += randomBlocks(journaldate)
    r = random.randint(0, 100)
    if r > 50:
        journal += addScheduled(journaldate)
    elif r < 20:
        journal += addDeadline(journaldate)
    homepage += '[['+LogseqDate(journaldate)+']]\n'
    return journal


def getRandomPageName():
    global pages
    nopages = len(pages)
    selectedpageindex = random.randint(0, nopages-1)
    if selectedpageindex > -1 and selectedpageindex <= nopages-1:
        return selectedpageindex
    else:
        return -1


def getRandomJournalPageName():
    nojournals = len(journals)
    selectedjournalindex = random.randint(0, nojournals-1)
    if selectedjournalindex > -1 and selectedjournalindex <= nojournals-1:
        return selectedjournalindex
    else:
        return -1


def addRandomLinkToTask():
    global pages
    randomno = random.randint(0, 9)
    pageref = ''
    if randomno < 5:
        # Append references to other pages
        otherpageindex = getRandomPageName()
        if otherpageindex > -1:
            pageref = '[['+pages[otherpageindex]["pagename"]+']]'
            pageref = pageref.replace('%2F', "/")
    return pageref


def addRandomLinksToEndOfPages():
    global pages
    for page in pages:
        # Append references to other pages
        otherpageindex = getRandomPageName()
        if otherpageindex > -1:
            if pages[otherpageindex]["pagename"] != page['pagename']:
                pagecontent = page["content"]
                pagecontent += '\n### Links to other pages\n'
                pageref = '[['+pages[otherpageindex]["pagename"]+']]'
                pageref = pageref.replace('%2F', "/")
                pagecontent += pageref+'\n'
                page["content"] = pagecontent
    return


def addRandomLinksToEndOfJournals():
    global journals
    for journal in journals:
        # Append references to other pages
        otherjournalindex = getRandomJournalPageName()
        if otherjournalindex > -1:
            if journals[otherjournalindex]["pagename"] != journal['pagename']:
                pagecontent = journal["content"]
                pagecontent += '\n### Links to other journals\n'
                pageref = '[[' + \
                    LogseqDate(journals[otherjournalindex]["pagename"])+']]'
                pageref = pageref.replace('_', "-")
                pagecontent += pageref+'\n'
                journal["content"] = pagecontent
    return


def addRandomPageLinksToTasks(marker):
    global pages, journals
    for journal in journals:
        randno = random.randint(0, 9)
        if randno < 3:
            otherpageindex = getRandomPageName()
            if otherpageindex > -1:
                pageref = pages[otherpageindex]["pagename"]
                pageref = pageref.replace('%2F', "/")
                journal["content"] = journal["content"].replace(
                    '\n- '+marker, '\n- '+marker+' [['+pageref+']]')
    for page in pages:
        randno = random.randint(0, 9)
        if randno < 5:
            if otherpageindex > -1:
                pageref = pages[otherpageindex]["pagename"]
                pageref = pageref.replace('%2F', "/")
                page["content"] = page["content"].replace(
                    '\n- '+marker, '\n- '+marker+' [['+pageref+']]')
    return


def GraphStatistics():
    msg = '- [[Home]]\n'
    msg += '- ## Graph Folder: \n  - '+targetfolder+'\n\n'
    msg += '- ## Pages Groups Generated\n'
    for pagegroup in PageGroupsToGenerate:
        ns = pagegroup['namespace']
        if ns == '':
            ns = 'none'
        msg += '\n  - '+pagegroup['title']
        msg += '\n    - namespace: '+ns
        msg += '\n    - page prefix: '+pagegroup['pageprefix']
        msg += '\n    - no of pages: '+str(pagegroup['nopages'])

    msg += '\n\n- ## Journals Generated'

    msg += '\n  - from date: '+JournalsToGenerate['fromdate']
    msg += '\n  - to date: '+JournalsToGenerate['todate']
    msg += '\n  - no journals: '+str(JournalsToGenerate['nojournals'])
    msg += '\n  - max increment in days: ' + \
        str(JournalsToGenerate['maxincrementindays'])

    if AddQueryPages:
        msg += '\n\n## Query Examples Pages Generated\n'
        msg += ' - no of examples: '+str(len(td.QueryTestCases))+'\n '

    msg += '\n\n'
    return msg


def QueryTestingPage():
    msg = ''
    msg += '- Query Testing is performed using the online advanced query testing tool at https://adxsoft.github.io/logseqadvancedquerybuilder/ \n'
    msg += '   - Follow the *how to use* instructions in the FAQ section of the online tool web page\n'
    msg += '- Paste the advanced queries you generate into a block using Cmd/Ctrl Shift V'
    msg += '   - *Tips. Hold Shift and click the Page Title to put this page in the right panel*'
    msg += '   - *      Examples are in the pages that start with "Query "'

    msg += '\n\n- Embedded Online Tool '
    msg += '- <iframe src="https://adxsoft.github.io/logseqadvancedquerybuilder/" allow="clipboard-read; clipboard-write" style="width: 100%; height: 1000px"></iframe>'
    msg += '\n\n'
    return msg


def createLogseqGraph():
    global targetfolder

    clearTargetFolder(targetfolder)

    for pagegroup in PageGroupsToGenerate:
        addPages(
            targetfolder,
            nopages=int(pagegroup['nopages']),
            namespace=pagegroup['namespace'],
            pageprefix=pagegroup['pageprefix']
        )

    # add query example pages
    addQueryPages(targetfolder)

    # add Journals
    addJournals(targetfolder,
                nojournals=JournalsToGenerate['nojournals'],
                increment=JournalsToGenerate['maxincrementindays'],
                fromdate='2020_01_01',
                todate='2023_12_31')

    # append links to other pages at the end of various pages
    addRandomLinksToEndOfPages()

    # append links to other journals at the end of various journals
    addRandomLinksToEndOfJournals()

    # append page links to various TODO tasks
    addRandomPageLinksToTasks('TODO')

    # append page links to various WAITING tasks
    addRandomPageLinksToTasks('WAITING')

    # write all pages to pages folder
    for page in pages:
        with open(targetfolder+'/pages/'+page["pagename"]+'.md', 'w') as f:
            f.write(page["content"])
        f.close()

    # write all journals to journals folder
    for journal in journals:
        with open(targetfolder+'/journals/'+journal["pagename"]+'.md', 'w') as f:
            f.write(journal["content"])
        f.close()

    # add Home Page
    with open(targetfolder+'/pages/Home.md', 'w') as f:
        f.write(homepage.replace('%2F', '/'))
        f.close()

    # add contents Page
    with open(targetfolder+'/pages/contents.md', 'w') as f:
        f.write(contentspage.replace('%2F', '/'))
        f.close()

    # add graph statistics Page
    with open(targetfolder+'/pages/Graph Statistics.md', 'w') as f:
        f.write(GraphStatistics())
        f.close()

    # add query testing page
    with open(targetfolder+'/pages/Query Testing.md', 'w') as f:
        f.write(QueryTestingPage())
        f.close()

    print('logseq Graph created in folder ~/LogseqTestGraph'+targetfolder)
    # print(GraphStatistics())
    if AddQueryPages:
        print('\nNote. The generated graph includes pages with advanced query examples')


# ==== MAIN ENTRY POINT =========

createLogseqGraph()
