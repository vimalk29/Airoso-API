package com.aeroso.aerosoapi.controllers.admin;


import com.aeroso.aerosoapi.payload.request.AirosoIndex;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@CrossOrigin(origins = "*", maxAge = 3600)
@RestController
@RequestMapping("/admin")
public class AdminController {

    private static final Logger logger = LoggerFactory.getLogger(AdminController.class);

    @PostMapping("/add-airosol-indices")
    @PreAuthorize("hasRole('ADMIN')")
    public String addAirosolIndices(@RequestBody List<AirosoIndex> indices) {
        for (AirosoIndex i: indices) {
            logger.info(i.toString());
        }
        return "Success.";
    }
}
