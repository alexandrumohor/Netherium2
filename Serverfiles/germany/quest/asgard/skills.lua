quest reset_scroll begin
    state start begin	
		when 71002.use begin        		
            say_title("Resetare competenşe:")
			say("")
            say("Gândeºte-te bine înainte sã faci asta!")
            say("Cu acest pergament işi vei reseta toate")
            say("competenşele." )
			say("" )
            say("Eºti sigur cã vrei acest lucru?")
			say("" )			
            local s = select("Da", "Nu")
			
				if 2 == s then 
					return
				end
			
				say_title("Resetare competenşe:")
				say("")
				say("Aceastã acşiune este ireversibilã.")
				say("Esti sigur?")
				say("")	
				local c = select("Da, reseteazã ","Nu")
			
				if 2 == c then
					return
				end
			
            say_title("Resetare competenşe:")		
			say("")
			say("Competenşele tale au fost resetate.")
			say("")
			pc.remove_item(71002)
            pc.clear_skill()
            pc.set_skill_group(0)			
        end
		
		
        when 71003.use begin  	
            say_title("Resetare competenşã:")
			say("")
            say("Acest pergament işi permite sã resetezi")
            say("o competenşã la 0 puncte.")
			say("Acestã acşiune este ireversibilã.")	
			say("")
			wait ()
			say("Alege competenşa:")		
			say("")
            local result = BuildSkillList(pc.get_job(), pc.get_skill_group())
            local vnum_list = result[1]
            local name_list = result[2]
            if table.getn(vnum_list) < 2 then
	
            say_reward("Nu ai competenşe pe care sã le poşi reseta.")
			say("")
                return
            end 
				
            local i = select_table(name_list)
			
            if table.getn(name_list) == i then
                return
            end
			
            local name = name_list[i]
            local vnum = vnum_list[i]
			
            say_title("Resetare competenşã:")
			say("")
            say(string.format("Eºti sigur cã vrei sã restezi %s ?", name))
			say("")
		    local s = select("Da", "Nu")
			
            if 2 == s then
                return
            end
			
			pc.remove_item(71003)
            pc.clear_one_skill(vnum)
            pc.setqf("force_to_master_skill", 1)
            say_title("Resetare competenşã:")
			say("")
            say("Competenşa a fost resetatã cu succes.")
			say("")			
        end
		
    end
end
