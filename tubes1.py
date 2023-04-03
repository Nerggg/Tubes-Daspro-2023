# Buka file CSV dalam mode baca
with open('user.csv', 'r') as csv_file:
    # Baca isi file
    csv_data = csv_file.read()

    # Inisialisasi beberapa variabel
    usernames = []
    passwords = []
    roles = []
    current_column = ''
    current_row = ''
    in_quotes = False

    # Iterasi setiap karakter dalam data CSV
    for char in csv_data:
        # Periksa apakah saat ini berada di dalam string yang diapit oleh tanda kutip ("")
        if char == '"' and not in_quotes:
            in_quotes = True
        elif char == '"' and in_quotes:
            in_quotes = False

        # Periksa apakah sudah mencapai akhir kolom
        if char == ',' and not in_quotes:
            current_row += current_column.strip() + ';'
            current_column = ''
        elif char == '\n' and not in_quotes:
            current_row += current_column.strip()
            # Pisahkan data pada setiap baris menjadi list
            row_data = current_row.split(';')
            # Ambil setiap data pada list dan masukkan ke list usernames, passwords, dan roles
            usernames.append(row_data[0])
            passwords.append(row_data[1])
            roles.append(row_data[2])
            current_column = ''
            current_row = ''
        else:
            current_column += char

