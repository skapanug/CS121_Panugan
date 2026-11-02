from supabase import supabase

result = supabase.table("users").select("*").execute()

print(result)