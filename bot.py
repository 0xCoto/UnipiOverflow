import discord

# Έτη
etos = ['','1ου','2ου','3ου','4ου']

# Έτος 1
mathimata_etos1 = ['Ανάλυση I 📕', 'Αρχές Προγραμματισμού 📕', 'Εισαγωγή στην Επιστήμη των Υπολογιστών 📕', 'Λογική Σχεδίαση Ψηφιακών Συστημάτων 📕', 'Μαθηματικά των Υπολογιστών 📕', 'Τεχνολογίες Διαδικτύου 📕', 'Ανάλυση ΙΙ 📕', 'Αντικειμενοστρεφής Προγραμματισμός 📕', 'Αρχιτεκτονική Υπολογιστών 📕', 'Διακριτά Μαθηματικά 📕', 'Δομές Δεδομένων 📕', 'Εφαρμοσμένη Άλγεβρα 📕']
mathimata_etos1_str = ''
for (i, mathima) in enumerate(mathimata_etos1, start=1):
    mathimata_etos1_str = mathimata_etos1_str + '\n`['+str(i)+']`: '+str(mathima)

# Έτος 2
mathimata_etos2 = ['Αντικειμενοστραφής Ανάπτυξη Εφαρμογών 📕', 'Λειτουργικά Συστήματα 📕', 'Μαθηματικός Προγραμματισμός 📕', 'Μεταγλωττιστές 📕', 'Πιθανότητες και Στατιστική 📕', 'Αλγόριθμοι 📕', 'Αρχές και Εφαρμογές Σημάτων και Συστημάτων 📕', 'Βάσεις Δεδομένων 📕', 'Δίκτυα Υπολογιστών 📕', 'Πληροφορική στην Εκπαίδευση 📕', 'Προγραμματισμός στο Διαδίκτυο και τον Παγκόσμιο Ιστό 📕', 'Δίκαιο της Πληροφορικής 📓', 'Εφαρμογές Θεωρίας Γραφημάτων 📓', 'Μάνατζμεντ 📓', 'Παιδαγωγικά 📓', 'Επιχειρησιακή Στρατηγική 📓', 'Δυναμικά Συστήματα 📓', 'Εφαρμοσμένη Συνδυαστική 📓', 'Θεωρία Πληροφοριών και Κωδίκων 📓', 'Υπολογιστική Θεωρία Αριθμών 📓', 'Ξενόγλωσση Ορολογία της Πληροφορικής 📓']
mathimata_etos2_str = ''
for (i, mathima) in enumerate(mathimata_etos2, start=1):
    mathimata_etos2_str = mathimata_etos2_str + '\n`['+str(i)+']`: '+str(mathima)

# Έτος 3
mathimata_etos3 = ['Αλληλεπίδραση Ανθρώπου και Υπολογιστή 📕', 'Αναγνώριση Προτύπων 📕', 'Πληροφοριακά Συστήματα 📕', 'Επιστημονική Συγγραφή στην Εκπαίδευση 📕', 'Τεχνολογία Λογισμικού 📕', 'Τεχνητή Νοημοσύνη και Έμπειρα Συστήματα 📕', 'Λογικός Προγραμματισμός 📘', 'Συστήματα Διαχείρισης Βάσεων Δεδομένων 📘', 'Προηγμένα Θέματα Επικοινωνιών 📗', 'Προηγμένη Αρχιτεκτονική Υπολογιστών 📗', 'Κρυπτογραφία 📙', 'Συστήματα Διαχείρισης Βάσεων Δεδομένων 📙', 'Ειδικά Θέματα Επιχειρησιακής Έρευνας 📓', 'Λογισμικό Διαχείρισης Μάθησης 📓', 'Θεωρία Παιγνίων & Εφαρμογές 📓', 'Θεωρία Υπολογισμού 📓', 'Βιοπληροφορική 📘', 'Επεξεργασία Φυσικής Γλώσσας 📘', 'Συστήματα Πολυμέσων 📘', 'Δίκτυα Υψηλών Ταχυτήτων 📗', 'Προγραμματισμός Συστημάτων, Τηλεπικοινωνιών και Υπηρεσιών 📗', 'Σχεδίαση Υπολογιστικών Συστημάτων 📗', 'Αναλυτική Δεδομένων 📙', 'Συστήματα Υποστήριξης Αποφάσεων 📙', 'Συστημική Ανάλυση 📙', 'Συστήματα Υποστήριξης Ομάδων 📓', 'Ευφυής Αλληλεπίδραση με Κοινωνικά Δίκτυα 📓', 'Διδακτική της Πληροφορικής 📓', 'Διοίκηση Ασφάλειας Συστημάτων 📓', 'Πρότυπα Ανάπτυξης Λογισμικού 📓']
mathimata_etos3_str = ''
for (i, mathima) in enumerate(mathimata_etos3, start=1):
    mathimata_etos3_str = mathimata_etos3_str + '\n`['+str(i)+']`: '+str(mathima)

# Έτος 4
mathimata_etos4 = ['Ανάλυση Εικόνας 📘', 'Εικονική Πραγματικότητα 📘', 'Σύγχρονα Θέματα Τεχνολογίας Λογισμικού - Λογισμικό για κινητές συσκευές 📘', 'Εκπαιδευτικό Λογισμικό 📘', 'Επεξεργασία Σημάτων Φωνής 📘', 'Ευφυείς Πράκτορες 📘', 'Ασφάλεια Πληροφοριακών Συστημάτων 📗📙', 'Κατανεμημένα και Πολυεπεξεργαστικά Πληροφοριακά Συστήματα 📗', 'Κινητές και Ασύρματες Επικοινωνίες 📗', 'Ασφάλεια Δικτύων 📗', 'Ηλεκτρονικό Επιχειρείν και Καινοτομία 📗', 'Πληροφοριακά Συστήματα στο Διαδίκτυο 📗',
                   'Ασφάλεια Πληροφοριακών Συστημάτων 📗', 'Ανάκτηση Πληροφορίας και Αναζήτηση στον Παγκόσμιο Ιστό 📙', 'Προσομοίωση Συστημάτων 📙', 'Διοικητική Πληροφορική 📙', 'Ηλεκτρονικό Επιχειρείν και Καινοτομία 📙', 'Πληροφοριακά Συστήματα στο Διαδίκτυο 📙', 'Υπολογιστική Γεωμετρία 📓', 'Υπηρεσιοστρεφές Λογισμικό 📓', 'Τεχνολογίες Ανάπτυξης Ηλεκτρονικών Παιχνιδιών 📓', 'Ηλεκτρονική Μάθηση & Κοινωνικά Δίκτυα 📓', 'Έξυπνες Πόλεις & Διαδίκτυο των Πραγμάτων 📓', 'Διαχείριση Γνώσης 📓', 'Γεωγραφικά Πληροφοριακά Συστήματα 📓', 'Αξιολόγηση Προγραμμάτων Διδασκαλίας 📓', 'Οχηματικά Δίκτυα Επόμενης Γενιάς 📓', 'Συστήματα Διασφάλισης Ποιότητας 📓', 'Συστήματα ERP - CRM 📓', 'Προηγμένα Θέματα Διαχείρισης Δικτύων και Κινητών Επικοινωνιών 📓', 'Τεχνολογίες Blockchain και Εφαρμογές 📓']
mathimata_etos4_str = ''
for (i, mathima) in enumerate(mathimata_etos4, start=1):
    mathimata_etos4_str = mathimata_etos4_str + '\n`['+str(i)+']`: '+str(mathima)

while True:
    token = 'xxx'
    client = discord.Client()
    
    @client.event
    async def on_ready():
        await client.change_presence(status=discord.Status.online, activity=discord.Game('Ψάχνεις παλαιότερα θέματα; 📖'))
        print(f'{client.user.name} has connected to Discord!')
    
    @client.event
    async def on_message(message):
        global observing
        print(message.content)
        if message.author == client.user:
            return
        if ((message.content).startswith('<@!892938') or (message.content).startswith('<@!892938') or ((message.content).lower()).startswith('@unipioverflow')) and '544370>' in message.content and 'view' not in (message.content).lower() and 'request' not in (message.content).lower():
            await message.channel.send('Το **UnipiOverflow** σου παρέχει θέματα παλαιότερων εξεταστικών για προσβάσιμη μελέτη. Κάνε ping <@!892938042191544370> για βοήθεια! 📝\n\n**Χρήση:**\n```@UnipiOverflow view <έτος>\n@UnipiOverflow request <έτος> <ID μαθήματος>\n@UnipiOverflow help\n```\n**Παραδείγματα:**\n```@UnipiOverflow view 2\n@UnipiOverflow request 12```\n**Git:** <https://github.com/0xCoto/UnipiOverflow> 📚 Built by <@!234246004424179712>')
            return
        if ((message.content).startswith('<@!892938') or (message.content).startswith('<@!892938') or ((message.content).lower()).startswith('@unipioverflow')) and '544370>' in message.content and len(message.content.split()) == 3 and (((message.content).split())[1]).lower() == 'view':
            if message.content.split()[2].isdigit() and int(message.content.split()[2]) >= 1 and int(message.content.split()[2]) <= 4:
                await message.add_reaction('📚')
                mathimata_etos = ''
                if str(message.content.split()[2]) == '1':
                    mathimata_etos = mathimata_etos1_str
                elif str(message.content.split()[2]) == '2':
                        mathimata_etos = mathimata_etos2_str
                elif str(message.content.split()[2]) == '3':
                        mathimata_etos = mathimata_etos3_str
                elif str(message.content.split()[2]) == '4':
                        mathimata_etos = mathimata_etos4_str
                await message.channel.send(
                    '<@!'+str(message.author.id)+ '> __Ορίστε τα μαθήματα του **'+etos[int(message.content.split()[2])]+'** έτους:__'+mathimata_etos+'\n——————————————————————————————\n**Κορμού** 📕 — **ΤΛΕΣ** 📘 — **ΔΥΣ** 📗 — **ΠΣΥ** 📙 — **Επιλογής** 📓')  #, file=discord.File(message.content.split()[2]+'/plot.png'))
        if ((message.content).startswith('<@!892938') or (message.content).startswith('<@!892938') or ((message.content).lower()).startswith('@unipioverflow')) and '544370>' in message.content and len(message.content.split()) == 4 and (((message.content).split())[1]).lower() == 'request':
            if message.content.split()[2].isdigit() and int(message.content.split()[2]) >= 1 and int(message.content.split()[2]) <= 4 and message.content.split()[3].isdigit():
                await message.add_reaction('🔎')
                mathimata_etos = ''
                if str(message.content.split()[2]) == '1':
                    mathimata_etos = mathimata_etos1
                elif str(message.content.split()[2]) == '2':
                        mathimata_etos = mathimata_etos2
                elif str(message.content.split()[2]) == '3':
                        mathimata_etos = mathimata_etos3
                elif str(message.content.split()[2]) == '4':
                        mathimata_etos = mathimata_etos4
                await message.channel.send('<@!'+str(message.author.id)+ '> Αναζήτηση παλαιών θεμάτων για **__'+mathimata_etos[int(message.content.split()[3])-1].replace(' 📕', '').replace(' 📘', '').replace(' 📗','').replace(' 📙', '').replace(' 📓', '')+'__**...')
                if True: ###### TO-DO: REPLACE CONDITION WITH IF >0 FILES EXISTS, SHOW HOW MANY/WHICH YEARS
                    tmp = True
                else:
                    await message.add_reaction('❌')
                    await message.channel.send('Δυστυχώς δεν κατάφερα να εντοπίσω θέματα παλαιότερων εξεταστικών. 😦')

    client.run(token)
