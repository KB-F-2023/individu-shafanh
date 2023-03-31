def color_map(adj_list, colors):
    # adj_list adalah kamus yang mewakili daftar kedekatan grafik
    # colors adalah daftar warna yang tersedia
    
    # Inisialisasi peta warna tanpa warna yang ditetapkan
    color_map = {node: None for node in adj_list.keys()}
    
    # Tentukan fungsi pembantu untuk memeriksa apakah suatu warna valid untuk node yang diberikan
    def is_valid_color(node, color):
        for neighbor in adj_list[node]:
            if color_map[neighbor] == color:
                return False
        return True
    
    # Tentukan fungsi backtracking rekursif
    def backtrack(node):
        # Base case: jika semua node telah diberi warna, return True
        if node is None:
            return True
        
        # Coba tetapkan setiap warna ke node saat ini
        for color in colors:
            if is_valid_color(node, color):
                color_map[node] = color
                if backtrack(next_node()):
                    return True
                color_map[node] = None
        
        # Jika tidak ada penetapan warna yang mengarah ke solusi, backtrack
        return False
    
    # Tentukan fungsi untuk mendapatkan node tidak berwarna berikutnya
    def next_node():
        for node, color in color_map.items():
            if color is None:
                return node
        return None
    
    # Mulai algoritma backtracking dari node pertama
    backtrack(next_node())
    
    return color_map

# Tentukan daftar adjacency untuk grafik dengan empat node
adj_list = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['NSW', 'SA'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V', 'T'],
    'T': ['SA']
}

# Tentukan daftar warna yang tersedia
colors = ['red', 'green', 'blue']

# Menyelesaikan coloring problem
color_map = color_map(adj_list, colors)

# Print hasil
print(color_map)

