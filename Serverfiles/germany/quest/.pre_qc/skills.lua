quest reset_scroll begin
    state start begin	
		when 71002.use begin        		
            say_title("Resetare competen�e:")
			say("")
            say("G�nde�te-te bine �nainte s� faci asta!")
            say("Cu acest pergament i�i vei reseta toate")
            say("competen�ele." )
			say("" )
            say("E�ti sigur c� vrei acest lucru?")
			say("" )			
            local s = select("Da", "Nu")
			
				if 2 == s then 
					return
				end
			
				say_title("Resetare competen�e:")
				say("")
				say("Aceast� ac�iune este ireversibil�.")
				say("Esti sigur?")
				say("")	
				local c = select("Da, reseteaz� ","Nu")
			
				if 2 == c then
					return
				end
			
            say_title("Resetare competen�e:")		
			say("")
			say("Competen�ele tale au fost resetate.")
			say("")
			pc.remove_item(71002)
            pc.clear_skill()
            pc.set_skill_group(0)			
        end
		
		
        when 71003.use begin  	
            say_title("Resetare competen��:")
			say("")
            say("Acest pergament i�i permite s� resetezi")
            say("o competen�� la 0 puncte.")
			say("Acest� ac�iune este ireversibil�.")	
			say("")
			wait ()
			say("Alege competen�a:")		
			say("")
            local result = BuildSkillList(pc.get_job(), pc.get_skill_group())
            local vnum_list = result[1]
            local name_list = result[2]
            if table.getn(vnum_list) < 2 then
	
            say_reward("Nu ai competen�e pe care s� le po�i reseta.")
			say("")
                return
            end 
				
            local i = select_table(name_list)
			
            if table.getn(name_list) == i then
                return
            end
			
            local name = name_list[i]
            local vnum = vnum_list[i]
			
            say_title("Resetare competen��:")
			say("")
            say(string.format("E�ti sigur c� vrei s� restezi %s ?", name))
			say("")
		    local s = select("Da", "Nu")
			
            if 2 == s then
                return
            end
			
			pc.remove_item(71003)
            pc.clear_one_skill(vnum)
            pc.setqf("force_to_master_skill", 1)
            say_title("Resetare competen��:")
			say("")
            say("Competen�a a fost resetat� cu succes.")
			say("")			
        end
		
    end
end
